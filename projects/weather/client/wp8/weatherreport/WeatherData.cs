using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace weatherreport
{
    public class CityData
    {
        public int m_iCityCode { get; set; }
        public string m_strCityCname { get; set; }
        public string m_strCityPinying { set; get; }
    }

    public class CurrentData
    {
        public Byte m_ucWeather { get; set; }
        public Byte m_ucTemperature { get; set; }
        public Byte m_ucWindDirect { get; set; }
        public Byte m_ucWindPower { get; set; }
        public Byte m_ucHimudity { get; set; }
    }
}
