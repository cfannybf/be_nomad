<template>
  <div class="searchresults">
    <div class="container" id="search_result">
      <div class="row">
        <h5 class="center">Search results</h5>
      </div>

      <div class="row">
        <div class="col s4" v-for="n in 7">
          <div class="card light-blue lighten-4">
            <div class="card-content grey-text text-darken-1">
              <span class="card-title">Job title</span>
              <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur dolor erat, bibendum
                sed tortor nec,
                consequat sollicitudin ex.
              </p>
              <p class="tags">Lorem Ipsum# Dolor++ Sit Amet</p>
            </div>
            <div class="card-action">
              <a href="#">Link</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SearchResults"
};
</script>
