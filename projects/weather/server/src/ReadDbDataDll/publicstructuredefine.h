#include <string>
#include<map>


using namespace std;

namespace DbStruct
{
	enum DAYENUM // ��������ö��ֵ�����X��
	{
		YES,
		DAY1,
		DAY2,
		DAY3,
		DAY4,
		DAY5,
		DAY6,
	};

	enum DAYTEMPENUM // ������������ö��ֵ�����X�����/���
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
		unsigned long m_ulCityId; // ����ID
		string m_strCityName; // ������������ 
		string m_strCityEnName; // ����Ӣ������
		string m_strCurDate; // ��ǰ����
		string m_strCurWeek; // ��ǰ�ܼ�
		string m_strFchh; // Ŀǰ���õ��ֶ�
	};

	struct WeatherDesc
	{
		unsigned long m_ulCityId; // ����ID
		map<DAYENUM, char> m_mapWeatherDesc; // ��¼7�����������ö��ֵ
	};

	struct WeatherWind
	{
		unsigned long m_ulCityId; // ����ID
		map<DAYENUM, char> m_mapWeatherWind; // ��¼7��ķ�������ö��ֵ
	};

	struct WeatherTemp
	{
		unsigned long m_ulCityId; // ����ID
		map<DAYTEMPENUM, char> m_mapWeatherTemp; // ��¼7�����������ö��ֵ
	};

	struct WeatherOtherInfo
	{
		unsigned long m_ulCityId; // ����ID
		string m_strCurClothesIndex; // ��ǰ����ָ��
		string m_strCurClothesIndexDesc; // ��ǰ����ָ����ϸ����
		string m_str48ClothesIndex; // δ��48Сʱ����ָ��
		string m_str48ClothesIndexDesc; // δ��48Сʱ����ָ����ϸ����
		string m_strCurUvIndex; // ��ǰ������ָ��
		string m_str48UvIndex; // δ��48Сʱ������ָ��
		string m_strWashCarIndex; // ϴ��ָ��
		string m_strTravelIndex; // ����ָ��
		string m_strComfortIndex; // ����ָ��
	};
}