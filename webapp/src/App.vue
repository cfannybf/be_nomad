<template>
  <div id="app">
    <FrontPage />
    <SearchResults />
    <FooterComponent />
  </div>
</template>

<script>
import FrontPage from "./components/FrontPage.vue";
import SearchResults from "./components/SearchResults.vue";
import FooterComponent from "./components/FooterComponent.vue";

export default {
  name: "app",
  components: {
    FrontPage,
    SearchResults,
    FooterComponent
  }
};
</script>

<style>
nav ul a,
nav .brand-logo {
  color: #e8eaf6;
}

p {
  line-height: 2rem;
}

.sidenav-trigger {
  color: #26a69a;
}

.tags {
  font-weight: bold;
  font-family: monospace;
  padding-top: 20px;
}

.parallax-container {
  min-height: 847px;
  line-height: 0;
  height: auto;
  color: rgba(255, 255, 255, 0.9);
}
.parallax-container .section {
  width: 100%;
  padding-top: 10%;
}

.image {
  opacity: 1 !important;
}

@media only screen and (max-width: 992px) {
  .parallax-container .section {
    position: absolute;
    top: 1%;
  }
  #index-banner .section {
    top: 1%;
  }
}

@media only screen and (max-width: 600px) {
  #index-banner .section {
    top: 0;
  }
}

.icon-block {
  padding: 0 15px;
}
.icon-block .material-icons {
  font-size: inherit;
}

footer.page-footer {
  margin: 0;
}
</style>