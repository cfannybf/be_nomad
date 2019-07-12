<template>
  <div class="frontpage">
    <NavBar />
    <div id="index-banner" class="parallax-container">
      <div class="section no-pad-bot">
        <div
          class="container scale-transition"
          id="get_started"
          v-bind:class="{ 'scale-out': state, hidden: state }"
        >
          <br />
          <br />
          <h1 class="header center light-blue-text text-lighten-4">be nomad.</h1>
          <div class="row center">
            <h5 class="header col s12 light">
              Begin your adventure of a lifetime. Find a remote job. Become a
              digital
              nomad.
            </h5>
          </div>
          <div class="row center">
            <a
              href="#"
              id="get_started_button"
              class="btn-large waves-effect waves-light light-blue darken-4"
              v-on:click="toggleState"
            >
              Get
              Started
            </a>
          </div>
          <br />
          <br />
        </div>

        <div
          class="container scale-transition scale-out"
          id="search_bar"
          v-bind:class="{ 'scale-in': state, 'scale-out': !state }"
        >
          <br />
          <br />
          <h1 class="header center light-blue-text text-lighten-4">Search</h1>
          <div class="row center">
            <form class="col s12">
              <div class="row">
                <div class="input-field col s12">
                  <input id="keywords" type="text" v-model="keywords" />
                  <label for="kewords">Keywords</label>
                </div>
                <div v-if="errors.length">
                  <label class="left error-message red-text text-lighten-1">{{errors}}</label>
                </div>
              </div>
            </form>
          </div>
          <div class="row center">
            <a
              id="download-button"
              class="btn-large waves-effect waves-light light-blue darken-4"
              v-on:click="search"
            >Find</a>
          </div>
          <br />
          <br />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import NavBar from "./NavBar.vue";

export default {
  name: "FrontPage",
  data() {
    return {
      state: false,
      keywords: "",
      errors: ""
    };
  },
  methods: {
    toggleState: function() {
      this.state = !this.state;
    },
    search: function() {
      this.errors = "";
      if (!this.keywords) {
        this.errors += "Empty search. ";
        return;
      }
      if (!this.validKeywords()) {
        this.errors += "Invalid search string. ";
        return;
      }
      axios
        .get("http://127.0.0.1:5002/search?keywords=" + this.keywords)
        .then(response => this.$root.$emit('search', response));
    },
    validKeywords: function() {
      var re = /^[a-zA-Z0-9,\.\+\-#]+$/;
      return re.test(this.keywords);
    }
  },
  components: {
    NavBar
  }
};
</script>

<style scoped>
.hidden {
  display: none;
}

.frontpage {
  background-image: url("../assets/back_1.jpeg");
}
.error-message {
  padding-left: 0.75rem;
}
</style>