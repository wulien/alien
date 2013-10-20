using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Navigation;
using Microsoft.Phone.Controls;
using Microsoft.Phone.Shell;
using weatherreport.Resources;

using System.Windows.Media.Imaging;
using System.Windows.Media;
using System.Xml;
using System.Threading.Tasks;
using System.IO;
using System.Threading;
using System.IO.IsolatedStorage;
using System.Xml.Linq;

namespace weatherreport
{
    public partial class MainPage : PhoneApplicationPage
    {
        public bool m_bCitySeted = false;
        public bool m_bHasData = false;
        public int m_iCurrentCityCode;
        public CurrentData m_stCuurentData;


        // 构造函数
        public MainPage()
        {
            InitializeComponent();

            // 用于本地化 ApplicationBar 的示例代码
            BuildLocalizedApplicationBar();

            SetBackGround();
            SetCityName();
            BuildTitle();
            TestXmlRead();

            LoadSavedData();

            SetDetailInfoState(Visibility.Collapsed);
            SetDetailInfoPanelState(Visibility.Collapsed);
        }

        void LoadSavedData()
        {
        }

        void SetDetailInfoPanelState(Visibility enumState)
        {
            page_day_detail.Visibility = enumState;
        }

        void SetDetailInfoState(Visibility enumState)
        {
            detail_icon.Visibility = enumState;
            detail_weekday.Visibility = enumState;
            detail_tempretuer.Visibility = enumState;
            detail_data.Visibility = enumState;
            detail_wind.Visibility = enumState;
            detail_weather.Visibility = enumState;
        }

        void SetPrefInfoState(Visibility enumState)
        {
            page_day1.Visibility = enumState;
            page_day1_icon.Visibility = enumState;
            day1_weekday.Visibility = enumState;
            day1_tempretuer.Visibility = enumState;

            page_day2.Visibility = enumState;
            page_day2_icon.Visibility = enumState;
            day2_weekday.Visibility = enumState;
            day2_tempretuer.Visibility = enumState;

            page_day3.Visibility = enumState;
            page_day3_icon.Visibility = enumState;
            day3_weekday.Visibility = enumState;
            day3_tempretuer.Visibility = enumState;

            page_day4.Visibility = enumState;
            page_day4_icon.Visibility = enumState;
            day4_weekday.Visibility = enumState;
            day4_tempretuer.Visibility = enumState;
        }

        private void TestXmlRead()
        //        public async Task ReadFromFile()
        {
            List<CityData> listLevels = new List<CityData>();
            try
            {
                XmlReaderSettings settings = new XmlReaderSettings();
                settings.Async = true;

                FileStream stream = File.OpenRead("cityAndCode.xml");
                using (XmlReader reader = XmlReader.Create(stream, settings))
                {
                    //                      while (await reader.ReadAsync())

                    while (reader.Read())
                    {
                        if (reader.NodeType == XmlNodeType.Element && reader.Name == "row")
                        {
                            CityData stCity = new CityData();
                            while (reader.Read())
                            {
                                if (reader.NodeType == XmlNodeType.EndElement && reader.Name == "row")
                                {
                                    listLevels.Add(stCity);
                                    break;
                                }

                                if (reader.NodeType == XmlNodeType.Element && reader.Name == "city")
                                {
                                    reader.Read();
                                    stCity.m_strCityCname = reader.Value;
                                }

                                if (reader.NodeType == XmlNodeType.Element && reader.Name == "code")
                                {
                                    reader.Read();
                                    stCity.m_iCityCode = Convert.ToInt32(reader.Value);
                                }

                                if (reader.NodeType == XmlNodeType.Element && reader.Name == "cityEn")
                                {
                                    reader.Read();
                                    stCity.m_strCityPinying = reader.Value;
                                }
                            }
                        }
                    }
                }
            }
            catch (Exception ex)
            {
                System.Diagnostics.Debug.WriteLine(string.Format(@"{0}:{1}", this.ToString(), ex.Message));
            }
        }

        private void SetCityName()
        {
            this.cname.Text = "武汉";
            this.ename.Text = "WuHan";
        }

        private void SetBackGround()
        {
            BitmapImage oBitmapBack;
            oBitmapBack = new BitmapImage(new Uri("/weatherreader;component/Assets/Resources/WeatherAnimation/sunnyWBG.jpg", UriKind.Relative));
            ImageBrush imageBrush = new ImageBrush();
            imageBrush.ImageSource = oBitmapBack;
            imageBrush.Stretch = System.Windows.Media.Stretch.UniformToFill;
            this.LayoutRoot.Background = imageBrush;

            page_day1_icon.Source = new BitmapImage(new Uri("/weatherreader;component/Assets/Resources/Images/WeatherSmall/bNight.2.png", UriKind.Relative));
        }

        // 用于生成本地化 ApplicationBar 的示例代码
        private void BuildLocalizedApplicationBar()
        {
            // 将页面的 ApplicationBar 设置为 ApplicationBar 的新实例。
            ApplicationBar = new ApplicationBar();
            ApplicationBar.Opacity = 0.5;

            // 创建新按钮并将文本值设置为 AppResources 中的本地化字符串。
            ApplicationBarIconButton appBarButton = new ApplicationBarIconButton(new Uri("/Assets/AppBar/appbar.add.rest.png", UriKind.Relative));
            appBarButton.Text = AppResources.AppBarButtonText;
            ApplicationBar.Buttons.Add(appBarButton);

            // 使用 AppResources 中的本地化字符串创建新菜单项。
            ApplicationBarMenuItem appBarMenuItem = new ApplicationBarMenuItem(AppResources.AppBarMenuItemText);
            ApplicationBar.MenuItems.Add(appBarMenuItem);
        }

        private void Income_Tile_Click(object sender, RoutedEventArgs e)
        {
            SetPrefInfoState(Visibility.Collapsed);
            SetDetailInfoPanelState(Visibility.Visible);
            storyBoard_prefclick.Begin();

            Dispatcher.BeginInvoke(() =>
            {
                Thread.Sleep(500);
                SetDetailInfoState(Visibility.Visible);
            });
        }

        private void DetailInfo_Click(object sender, RoutedEventArgs e)
        {
            SetDetailInfoState(Visibility.Collapsed);
            storyBoard_detailclick.Begin();
            Dispatcher.BeginInvoke(() =>
            {
                Thread.Sleep(500);
                SetPrefInfoState(Visibility.Visible);
            });
        }

        private void BuildTitle()
        {
            FlipTileData maintile = new FlipTileData
            {
                Title = "Flip Tile", // 标题
                Count = 0, // 数量
                BackgroundImage = new Uri("/Assets/Resources/Images/PinImage/Classical/Day.0.png", UriKind.Relative), // 中尺寸背景图
                BackTitle = "Back Flip Tile", // 背面标题
                BackContent = "Back Flip Tile Content", // 背面内容
                BackBackgroundImage = new Uri("/Assets/Resources/Images/PinImage/Classical/Day.1.png", UriKind.Relative), // 中尺寸背面背景图
                SmallBackgroundImage = new Uri("/Assets/Tiles/FlipCycleTileSmall.png", UriKind.Relative), // 小尺寸背景图
                WideBackgroundImage = new Uri("/Assets/Resources/Images/PinImage/Classical/Day.1.png", UriKind.Relative), // 大尺寸背景图
                WideBackContent = "Wide Back Flip Tile Content", // 大尺寸背面内容
                WideBackBackgroundImage = new Uri("/Assets/Resources/Images/PinImage/Classical/Day.1.png", UriKind.Relative), // 大尺寸背面背景图
            };

            ShellTile TileToFind = ShellTile.ActiveTiles.First();
            TileToFind.Update(maintile);
        }


        public string strResourceDir = "/Assets/Resources";
    }
}