<template>
  <div class="drinks">
    <h1>This page's with drinks rating</h1>

    <form @keydown.enter="onAddFormSubmit">
      <label>
        Drink name:
        <input type="text" v-model="new_name">
      </label>
      <br>
      <label>
        Description:
        <input type="text" v-model="new_description">
      </label>
      <br>
      <label>
        Drink rating:
        <input type="number" v-model="new_rating" min="0" max="10">
      </label>
      <br>
    </form>

    <table class="drinks-list">
      <thead>
      <tr>
        <th>Name</th>
        <th>Description</th>
        <th>Rating</th>
        <th>Remove</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="drink in drinks" v-bind:key="drink">
        <td>{{ drink.name }}</td>
        <td>{{ drink.description }}</td>
        <td>{{ drink.rating }}/10</td>
        <td>
          <button @click="removeDrink(drink)">-</button>
        </td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';

const BASE_API_URL = '/api/v1';

export default {
  name: 'ListDrinks',
  components: {},
  methods: {
    getDrinks() {
      const jwt = this.$cookies.get('jwt_token');
      const DRINKS_API_URL = `${BASE_API_URL}/drinks/`;
      const config = {
        headers: {
          Authorization: `Bearer ${jwt}`,
        },
      };

      const getData = axios.get(`${DRINKS_API_URL}`, config);
      alert(getData);
      getData.then((response) => {
        this.drinks = response.data;
      });
    },
    onAddFormSubmit(event) {
      event.preventDefault();
      const requestData = {
        name: this.new_name,
        description: this.new_description,
        rating: this.new_rating,
      };
      const csrf = this.$cookies.get('csrftoken');
      const jwt = this.$cookies.get('jwt_token');

      const config = {
        headers: {
          'X-CSRFToken': csrf,
          Authorization: `Bearer ${jwt}`,
        },
      };
      axios.post(`${BASE_API_URL}/drinks/`, requestData, config).then(() => {
        this.getDrinks();
      });
      this.new_name = '';
      this.new_description = '';
      this.new_rating = '';
    },
    removeDrink(drink) {
      const jwt = this.$cookies.get('jwt_token');
      const config = {
        headers: {
          Authorization: `Bearer ${jwt}`,
        },
      };
      const { id } = drink;
      axios.delete(`${BASE_API_URL}/drinks/${id}`, config).then(() => {
        this.getDrinks();
      });
    },
  },
  data() {
    return {
      drinks: {},
      new_name: '',
      new_description: '',
      new_rating: '',
    };
  },
  mounted() {
    this.getDrinks();
  },
};
</script>

<style>
.drinks-list {
  border: 1px solid black;
  margin-left: auto;
  margin-right: auto;
}

.drinks-list > td {
  text-align: center;
}
</style>
