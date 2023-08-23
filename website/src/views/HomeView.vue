<script setup>
import { ref } from 'vue';
import { RouterLink } from 'vue-router';

const installLinkOfExtension = ref("https://microsoftedge.microsoft.com/addons/detail/tampermonkey/iikmkjmpaadaobahmlepeloendndfphd");
</script>

<template>
  <el-main>
    <div class="welcome-container">
      <div class="welcome-text">
        <h2>欢迎来到“无障碍优化平台”</h2>
        <p>这是一个以技术手段解决网页无障碍问题的平台，旨在帮助障碍人士顺畅地使用各种网站。</p>
        <p>平台上提供有各种网站的无障碍优化脚本，这些脚本由 JavaScript 编写，可以在指定的网页中运行。</p>
        <p>为了使用这些脚本，您需要先在浏览器内安装我们的扩展插件。
          <el-link type="primary" :href="installLinkOfExtension">立即去安装</el-link>。
        </p>
        <p>（注：平台的扩展插件还未上架，暂时使用 Tampermonkey 替代） </p>
        <p>您可以自由地挑选和安装平台上的脚本，<router-link to="/scripts">点此进入脚本库</router-link>。</p>
        <p>如果您遇到了网页的无障碍问题，可以发布在我们的平台，平台上的开发者看到后，会尝试编写无障碍脚本解决您的问题。<router-link to="/need_upload">点此立即发布需求</router-link>。
        </p>
        <p>如果您是一名开发者，想要为信息无障碍做出贡献，我们将十分欢迎。您可以<router-link to="/needs">浏览障碍用户的需求</router-link>，或者<router-link
            to="/script_upload">上传您编写的无障碍优化脚本</router-link>。</p>
      </div>
    </div>
  </el-main>
</template>

<style scoped>
.welcome-container {
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

/*
.welcome-text {
  text-align: center;
}
*/
</style>