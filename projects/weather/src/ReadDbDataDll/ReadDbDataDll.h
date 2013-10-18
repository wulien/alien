#ifndef READDBDATADLL_H_
#define READDBDATADLL_H_

#ifdef READDBDATDLL
#define READDBDATDLL extern "C" _declspec(dllimport) 
#else
#define READDBDATDLL extern "C" _declspec(dllexport) 
#endif

#include <string>
#include <vector>
#include "publicstructuredefine.h"

using namespace std;
using namespace DbStruct;

READDBDATDLL int Add(int plus1, int plus2); // ���Ժ���

// ��ȡ���л�����Ϣ
READDBDATDLL bool ReadCityBasicInfo(const string &strCityName, CityBasicInfo &stCiyInfo);

// ��ȡ����������Ϣ
READDBDATDLL bool ReadWeatherDescInfo(const int &iCityId, WeatherDesc &stWeatherDescInfo);

// ��ȡ����������Ϣ
READDBDATDLL bool ReadWeatherWindInfo(const int &iCityId, WeatherWind &stWeatherWindInfo);

// ��ȡ�����¶���Ϣ
READDBDATDLL bool ReadWeatherTempInfo(const int &iCityId, WeatherTemp &stWeatherTempInfo);

// ��ȡ����������Ϣ
READDBDATDLL bool ReadWeatherOtherInfo(const int &iCityId, WeatherOtherInfo &stWeatherOtherInfo);

#endif