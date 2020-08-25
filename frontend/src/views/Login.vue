<template>
  <div class="login">
    <h2>Введите логин и пароль и нажмите [Enter]</h2>
    <form @keydown.enter="onSubmit">
      <label>
        Логин:
        <input type="text" v-model="username">
      </label>
      <br>
      <label>
        Пароль:
        <input type="password" v-model="password">
      </label>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

const AUTH_URL = '/api/token/';

export default {
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    onSubmit(event) {
      event.preventDefault();
      const requestData = {
        username: this.username,
        password: this.password,
      };
      const config = {
        headers: {
          'X-CSRFToken': this.$cookies.get('csrftoken'),
        },
      };
      axios.post(AUTH_URL, requestData, config).then((response) => {
        this.$cookies.set('jwt_token', response.data.access);
      });
      this.username = '';
      this.password = '';
    },
  },
};
</script>
