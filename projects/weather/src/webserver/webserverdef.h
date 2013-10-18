#pragma once

typedef char* xsd__string;
typedef int   xsd__int;
typedef unsigned char  xsd__byte;

//gsoap ns service name: weatherreader
//gsoap ns service style: rpc
//gsoap ns service encoding: encoded
//gsoap ns service namespace: http://threepepolego/services/weather.wsdl
//gsoap ns service location: http://localhost:8888

enum ns__WEATHERDEFINE
{
	SUN = 1,
};

struct ns__weatherinfo_current
{
	xsd__byte byteWeather;
	xsd__byte byteTemperature;
	xsd__byte byteHimudity;
	xsd__byte byteWindDirect;
	xsd__byte byteWindPower;
};

xsd__int ns__GetCurrWeatherInfo(xsd__int iCityCode,
struct ns__weatherinfo_current &stCurrWeatherInfo);