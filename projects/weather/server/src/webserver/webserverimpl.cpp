
#include "stdafx.h"
#include <boost/thread.hpp>
#include "stdsoap2.h"
#include "weatherreader.nsmap"
#include "webserverimp.h"

/************************************************************************/
/*      web service服务器                                               */
/************************************************************************/
SOAP_SOCKET* squeue = NULL;
int head = 0, tail = 0;

boost::mutex queue_cs;
boost::condition_variable queue_cv;

string G_STRSERVERIP = "10.84.11.88";
int G_IPORT = 8888;

void* process_queue(void*);
int enqueue(SOAP_SOCKET);
SOAP_SOCKET dequeue();
int http_get(struct soap* soap);

int iThreadNum = 100;
int iMaxQueueDepth = 1000;

int WebServiceRun(int argc, char* argv[])
{
	struct soap soap;
	soap_init(&soap);
	soap.fget = http_get;
	soap.accept_timeout = 1;
	struct soap** soap_thr = new struct soap*[iThreadNum];
	boost::thread_group tg;
	squeue = new SOAP_SOCKET[iMaxQueueDepth];
	SOAP_SOCKET m,s;
	int i;
	m = soap_bind(&soap, G_STRSERVERIP.c_str(), G_IPORT, iThreadNum);
	if( !soap_valid_socket(m) )
	{
		return 1;
	}

	for( i = 0; i < iThreadNum; i++ )
	{
		soap_thr[i] = soap_copy(&soap);
		tg.create_thread(boost::bind(&process_queue, (void*)soap_thr[i]));
	}

	unsigned int requestnum = 0;
	clock_t t1 = clock();
	for(;;)
	{
// 		if (g_evtStop.Wait(1))
// 		{
// 			break;
// 		}

		clock_t t2 = clock();
		s = soap_accept(&soap);
		if( !soap_valid_socket(s) )
		{
			if( soap.errnum )
			{
				char buf[128];
				soap_sprint_fault(&soap, buf, 128);
				return 1;
			}
			else
			{
				clock_t t3 = clock();
				//LOG4CPLUS_ERROR(logger, "server timed out:" << difftime(t3,t2)/1000 << "s");
				continue;
			}
		}
		char buf[16];
		sprintf(buf, "%d.%d.%d.%d", (soap.ip>>24)&0xff, (soap.ip>>16)&0xff, 
			(soap.ip>>8)&0xff, soap.ip&0xff);
		requestnum++;
		clock_t t4 = clock();
		double timeelapsed = 0;
		if( requestnum % 10 == 0 )
		{
			timeelapsed = difftime(t4,t1);
			if( timeelapsed > 0 )
			{
			}
		}
		while( enqueue(s) == SOAP_EOM )
			boost::this_thread::sleep(boost::posix_time::milliseconds(1));
		if( timeelapsed > 100000 )//至少100s统计一次
		{
			requestnum = 0;
			t1 = clock();
		}
	}
	for( i = 0; i < iThreadNum; i++ )
	{
		while( enqueue(SOAP_INVALID_SOCKET) == SOAP_EOM )
			boost::this_thread::sleep(boost::posix_time::milliseconds(1));
	}

	tg.join_all();
	for( i = 0; i < iThreadNum; i++ )
	{	
		soap_done(soap_thr[i]);
		free(soap_thr[i]);
	}

	soap_done(&soap);
	return 0;
}

void* process_queue(void* soap)
{
	struct soap* tsoap = (struct soap*)soap;
	for(;;)
	{
		tsoap->socket = dequeue();
		if( !soap_valid_socket(tsoap->socket) )
			break;
		soap_serve(tsoap);
		soap_destroy(tsoap);
		soap_end(tsoap);
	}
	return NULL;
}

int enqueue(SOAP_SOCKET sock)
{
	int status = SOAP_OK;
	int next;
	boost::unique_lock<boost::mutex> lock(queue_cs);
	next = tail + 1;
	if( next >= iMaxQueueDepth )
		next = 0;
	if( next == head )
		status = SOAP_EOM;
	else
	{
		squeue[tail] = sock;
		tail = next;
	}
	queue_cv.notify_one();
	return status;
}

SOAP_SOCKET dequeue()
{
	SOAP_SOCKET sock;
	boost::unique_lock<boost::mutex> lock(queue_cs);
	while( head == tail )
	{
		queue_cv.wait(lock);
	}
	sock = squeue[head++];
	if( head >= iMaxQueueDepth )
		head = 0;
	return sock;
}

int http_get(struct soap* soap)
{
	char* s = strchr(soap->path, '?');
	if( !s || strcmp(s, "?wsdl") )
		return SOAP_GET_METHOD;
	FILE* fd = fopen("..//dat//FIBERHOME_EPON_SERVICE.wsdl", "rb");
	if( !fd )
		return 404;
	soap->http_content = "text/xml";
	soap_response(soap, SOAP_FILE);
	for(;;)
	{
		size_t r = fread(soap->tmpbuf, 1, sizeof(soap->tmpbuf), fd);
		if( !r )
			break;
		if( soap_send_raw(soap, soap->tmpbuf, r) )
			break;
	}
	fclose(fd);
	soap_end_send(soap);
	return SOAP_OK;
}

/************************************************************************/
/*        web service接口实现                                           */
/************************************************************************/

int ns__GetCurrWeatherInfo(struct soap*, int iCityCode, struct ns__weatherinfo_current &stCurrWeatherInfo)
{
	stCurrWeatherInfo.byteHimudity =2;
	stCurrWeatherInfo.byteTemperature = 78;
	stCurrWeatherInfo.byteWeather = 3;
	stCurrWeatherInfo.byteWindDirect = 4;
	stCurrWeatherInfo.byteWindPower = 6;
	return SOAP_OK;
}