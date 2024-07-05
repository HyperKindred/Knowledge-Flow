<template>
  <div class="main">
    <div class="top">
      <img class="github" alt="github" src="@/assets/images/github.png">
      <h4>@github: https://github.com/HyperKindred/Knowledge-Flow</h4>
    </div>
    <div class="center">
      <div class="welcome-text">
        <h2>Welcome to KnowledgeFlow</h2>
        <h2>欢迎使用知流</h2>
      </div>
    </div>
    <div class="button">
      <div class="author">
        <div class="profile-item" v-for="author in authors" :key="author.name">
          <img class="profile" :alt="author.name" :src="author.img" />
          <h3>{{ author.name }}</h3>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import NinestateImg from '@/assets/images/Ninestate.jpg';
import HypercubeImg from '@/assets/images/Hypercube.jpg';
import FeBlueImg from '@/assets/images/FeBlue.jpg';
const authors = [
  { name: '@Ninestate', img: NinestateImg },
  { name: '@Hypercube', img: HypercubeImg },
  { name: '@FeBlue', img: FeBlueImg }
];
</script>

<style scoped>
.main {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  height: 98.5vh;
  width: 100%;
}

.center {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-grow: 1;
}

.welcome-text {
  text-align: center;
  color: beige;
}

.button {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 10px 0;
  background-color: rgba(0, 0, 0, 0.5);
}

.author {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
}

.profile-item {
  display: flex;
  align-items: center;
  margin: 0 30px;
}

.profile {
  height: 50px;
  width: auto;
  border-radius: 50%;
  margin-right: 10px;
}

.github {
  height: 30px;
  width: auto;
  border-radius: 50%;
  margin-right: 10px;
}

.author h3 {
  margin: 0;
  color: white;
}

.top {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  width: 100%;
  padding: 10px;
}

.top h4 {
  margin: 0;
  color: white;
}
</style>
