<template>
  <div>
    <h1>Users</h1>
    <ul>
      <li v-for="user in users" :key="user.id">{{user.id}} : {{user.name}}</li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data(){
    return {
      users: [],
    };
  },
  async created(){
    // const response = await axios.get("http://localhost:8080/users/read");
    const response = await axios.get("http://127.0.0.1:8000/users");
    this.users = response.data;
  }
}
</script>