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

READDBDATDLL int Add(int plus1, int plus2); // 测试函数

// 读取城市基本信息
READDBDATDLL bool ReadCityBasicInfo(const string &strCityName, CityBasicInfo &stCiyInfo);

// 读取天气描述信息
READDBDATDLL bool ReadWeatherDescInfo(const int &iCityId, WeatherDesc &stWeatherDescInfo);

// 读取天气风向信息
READDBDATDLL bool ReadWeatherWindInfo(const int &iCityId, WeatherWind &stWeatherWindInfo);

// 读取天气温度信息
READDBDATDLL bool ReadWeatherTempInfo(const int &iCityId, WeatherTemp &stWeatherTempInfo);

// 读取天气其他信息
READDBDATDLL bool ReadWeatherOtherInfo(const int &iCityId, WeatherOtherInfo &stWeatherOtherInfo);

#endif