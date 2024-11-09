<template>
  <div>
    <!-- Header Section -->
    <header class="bg-main header">
      <div class="logo margin-big-left fadein-top">
        <h1>旅游大数据分析平台</h1>
      </div>
      <div class="head-l">
        <button @click="refreshHome" class="button button-little bg-green">
          <span class="icon-home"></span> 刷新首页
        </button>
        <button @click="logout" class="button button-little bg-red">
          <span class="icon-power-off"></span> 退出系统
        </button>
      </div>
    </header>
  </div>
  <div class="leftnav">
    <div class="leftnav-title"><strong><span class="icon-list">菜单列表</span> </strong></div>
    <h2><span class="icon-user"></span>基本设置 </h2>
    <ul style="display: block">
      <li><router-link to="/hotspot" target="right"><span class="icon-caret-right"></span>热门景点分析</router-link></li>
      <li><router-link to="/tickets" target="right"><span class="icon-caret-right"></span>景点门票分析</router-link></li>
      <li><router-link to="/recommend" target="right"><span class="icon-caret-right"></span>旅游景点推荐</router-link></li>
      <li><router-link to="/emotion" target="right"><span class="icon-caret-right"></span>旅游舆情分析</router-link></li>
    </ul>

  </div>
  <div class="admin">
    <main>
    <router-view />
    </main>
  </div>
  <ul class="bread">
	<li><a href="${ctx}/hotspot/search" target="right" class="icon-home">首页</a> </li>
	<li><a href="#">网站信息</a> </li>
	<li><b>当前语言：</b><span style="color:#ff0000">中文</span>
		&nbsp;&nbsp;&nbsp;&nbsp;切换语言：<a href="#">中文</a>&nbsp;&nbsp;<a href="#">英文</a>
	</li>
</ul>
</template>

<script>
export default {
  name: 'IndexApp',
  methods: {
    refreshHome() {
      // Redirect to home page
      window.location.href = "/";
    },
    logout() {
      // Redirect to logout page or external link
      window.location.href = "https://cn.bing.com";
    },
  },
};
</script>

<style scoped>
/* Import your styles */
@import url('../public/css/pintuer.css');
@import url('../public/css/admin.css');

.bg-main {
  background-color: #f2f9fd;
}
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>
