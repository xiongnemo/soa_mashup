<template>
  <div class="mashup">
    <h1 id="soa-header">{{ msg }}</h1>
    <el-input
      placeholder="城市.."
      v-model="input"
      type="text"
      @keyup.enter.native="soa_search"
      id="soa_search_content"
      class="soa_search_content_text"
      clearable
    >
    </el-input>
    <el-button
      size="medium"
      @click.native="soa_search"
      class="soa_search_submit"
      type="primary"
      icon="el-icon-search"
      >搜索/提交</el-button
    ><el-button
      size="medium"
      @click.native="soa_search_test"
      class="soa_search_submit" icon="el-icon-magic-stick"
      >测试</el-button
    >
    <el-container
      style="
        background: linear-gradient(
          45deg,
          rgb(211, 220, 230),
          rgb(153, 169, 191)
        );
        width: 100%;
      "
      ><el-main>
        <el-row>
          <el-col :span="24"
            ><div v-loading="loading" class="grid-content bg-purple-dark">
              <br />
              <br />
              城市简介<br />
              <br /><el-main
                ><a
                  class="soa-exact-brief-information"
                  id="soa_city_brief_information_answer"
                >
                  {{ initial }}
                </a></el-main
              >
              <br /><br />
            </div>
          </el-col>
        </el-row>

        <el-row :span="24">
          <el-col :span="8"
            ><div v-loading="loading" class="grid-content bg-purple">
              <h3 class="h3"><br />位置</h3>
              <br />
              城市中心：
              <a class="soa-exact" id="soa_city_position_answer">
                {{ initial }}
              </a>
              <br /><br />
              <br />
            </div>
            <br />
            <br />
            <div v-loading="loading" class="grid-content bg-purple">
              <div class="amap-wrapper">
                <el-amap
                  class="amap-box"
                  :vid="'amap-vue'"
                  ref="map"
                  :plugin="plugin"
                  :center="amap_center_pos"
                  :zoom="zoom"
                ></el-amap>
              </div></div
          ></el-col>
          <el-col :span="8"
            ><div v-loading="loading" class="grid-content bg-purple">
              <h3 class="h3"><br />气象</h3>
              <br />
              当前天气：
              <a class="soa-exact" id="soa_city_weather_answer_weather">
                {{ initial }}
              </a>
              <br />
              <br />
              当前温度：
              <a class="soa-exact" id="soa_city_weather_answer_temp">
                {{ initial }}
              </a>
              <br />
              <br />
              今日最高温：
              <a class="soa-exact" id="soa_city_weather_answer_temp_high">
                {{ initial }}
              </a>
              <br />
              <br />
              今日最低温：
              <a class="soa-exact" id="soa_city_weather_answer_temp_low">
                {{ initial }}
              </a>
              <br />
              <br />
              当前 AQI 指数：
              <a class="soa-exact" id="soa_city_weather_answer_aqi">
                {{ initial }}
              </a>
              <br />
              <br />
              当前空气质量状态：
              <a class="soa-exact" id="soa_city_weather_answer_aqi_str">
                {{ initial }}
              </a>
              <br /><br /><br />
            </div>
            <div v-loading="loading" class="grid-content bg-purple">
              <h3 class="h3"><br />GDP</h3>
              <br />
              GDP 总量：
              <a class="soa-exact" id="soa_city_gdp_answer_gdp">
                {{ initial }}
              </a>
              <br />
              <br />
              数据时间：
              <a class="soa-exact" id="soa_city_gdp_answer_year">
                {{ initial }}
              </a>
              <br />
              <br />
            </div>
            <br /><br />
            <br
          /></el-col>
          <el-col :span="8"
            ><div v-loading="loading" class="grid-content bg-purple">
              <h3 class="h3">
                <br />新闻<br />
              </h3>
              <el-table id="soa_city_news_answer" :data="tableData">
                <el-table-column prop="news_title" label="标题" width="140">
                </el-table-column>
                <el-table-column prop="news_source" label="来源" width="80">
                </el-table-column>
                <el-table-column prop="news_contents" label="内容">
                </el-table-column>
                <el-table-column prop="news_time" label="时间" width="140">
                </el-table-column>
              </el-table></div
          ></el-col>
        </el-row> </el-main
    ></el-container>
  </div>
</template>

<style>
body {
  background: linear-gradient(45deg, rgb(211, 220, 230), rgb(153, 169, 191));
  -ms-overflow-style: none;  /* IE and Edge */
  scrollbar-width: none;  /* Firefox */
}

::-webkit-scrollbar {
  display: none;
}

.amap-wrapper {
  width: 100%;
  height: 500px;
}

.el-header {
  background-color: #b3c0d1;
  color: #333;
  line-height: 60px;
}

.el-aside {
  color: #333;
}

.el-input {
  width: 200px;
  margin: auto;
  background-position: center;
  text-align: center;
}

.el-row {
  margin-top: 50px;
  position: relative;
  margin-bottom: 20px;
  /* &:last-child {
    margin-bottom: 0;
  } */
}

.grid-content:hover {
  box-shadow: 0 14px 28px rgba(0, 0, 0, 0.25), 0 10px 10px rgba(0, 0, 0, 0.22);
}

.el-col {
  position: relative;
  padding-left: 1cm;
  padding-right: 1cm;
  border-radius: 2px;
  display: inline-block;
  position: relative;
}
.bg-purple-dark {
  background: #99a9bf;
}
.bg-purple {
  background: #d3dce6;
}
.bg-purple-light {
  background: #e5e9f2;
}

.grid-content {
  border-radius: 4px;
  position: relative;
  background-position: center;
  min-height: 80px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.24);
  transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
}

.h3 {
  text-align: center;
  margin-top: 20px;
}
.soa-exact-brief-information {
  padding-left: 10%;
  padding-right: 10%;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
</style>

<script>
export default {
  data() {
    return {
      tableData: Array(0),
      input: "",
      msg: "SOA mashup frontend",
      initial: "等待初始输入",
      amap_center_pos: [121.215281, 31.286028],
      zoom: 12,
      plugin: [
        {
          pName: "MapType",
          defaultType: 0,
          events: {
            init(o) {
              console.log(o);
            },
          },
        },
      ],
      loading: false,
    };
  },
  methods: {
    soa_search_test() {
      this.amap_center_pos = [121.215281, 31.286028];
      this.tableData = Array(0);
      // console.log(test);

      // test[0].style.visibility = "hidden";
      this.$soa_mashup_test(this.amap_center_pos, this.tableData);
    },
    soa_search() {
      var city_name = document.getElementById("soa_search_content").value;
      console.log(city_name);
      this.tableData = Array(0);
      this.$soa_mashup(city_name, this.amap_center_pos, this.tableData, this);

      // this.amap_center_pos = [121.215281, 31.286028]
      // this.$soa_city_position(city_name, this.amap_center_pos);
      // this.$soa_city_weather(city_name);
      // this.$soa_city_brief_information(city_name);
      // this.tableData = Array(0);
      // this.$soa_city_news(city_name, this.tableData);
      // this.$soa_city_gdp(city_name);
    },
  },
};
</script>



