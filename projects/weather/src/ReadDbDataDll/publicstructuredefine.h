#include <string>
#include<map>


using namespace std;

namespace DbStruct
{
	enum DAYENUM // 描述天数枚举值，如第X天
	{
		YES,
		DAY1,
		DAY2,
		DAY3,
		DAY4,
		DAY5,
		DAY6,
	};

	enum DAYTEMPENUM // 描述气温天数枚举值，如第X天最高/最低
	{
		YES_LOW,
		YES_HIGH,
		DAY1_LOW,
		DAY1_HIGH,
		DAY2_LOW,
		DAY2_HIGH,
		DAY3_LOW,
		DAY3_HIGH,
		DAY4_LOW,
		DAY4_HIGH,
		DAY5_LOW,
		DAY5_HIGH,
		DAY6_LOW,
		DAY6_HIGH,
	};

	struct CityBasicInfo
	{
		unsigned long m_ulCityId; // 城市ID
		string m_strCityName; // 城市中文名称 
		string m_strCityEnName; // 城市英文名称
		string m_strCurDate; // 当前日期
		string m_strCurWeek; // 当前周几
		string m_strFchh; // 目前无用的字段
	};

	struct WeatherDesc
	{
		unsigned long m_ulCityId; // 城市ID
		map<DAYENUM, char> m_mapWeatherDesc; // 记录7天的天气描述枚举值
	};

	struct WeatherWind
	{
		unsigned long m_ulCityId; // 城市ID
		map<DAYENUM, char> m_mapWeatherWind; // 记录7天的风向描述枚举值
	};

	struct WeatherTemp
	{
		unsigned long m_ulCityId; // 城市ID
		map<DAYTEMPENUM, char> m_mapWeatherTemp; // 记录7天的气温描述枚举值
	};

	struct WeatherOtherInfo
	{
		unsigned long m_ulCityId; // 城市ID
		string m_strCurClothesIndex; // 当前穿衣指数
		string m_strCurClothesIndexDesc; // 当前穿衣指数详细描述
		string m_str48ClothesIndex; // 未来48小时穿衣指数
		string m_str48ClothesIndexDesc; // 未来48小时穿衣指数详细描述
		string m_strCurUvIndex; // 当前紫外线指数
		string m_str48UvIndex; // 未来48小时紫外线指数
		string m_strWashCarIndex; // 洗车指数
		string m_strTravelIndex; // 旅游指数
		string m_strComfortIndex; // 舒适指数
	};
}