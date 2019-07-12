<template>
  <div class="searchresults" v-if="rendered">
    <div class="container" id="search_result">
      <div class="row">
        <h5 class="center">Search results</h5>
      </div>

      <div class="row">
        <div class="col s4" v-for="job in rendered">
          <div class="card light-blue lighten-4">
            <div class="card-content grey-text text-darken-1">
              <span class="card-title">{{job.company}}</span>
              <p>
                {{job.title}}
              </p>
              <p class="tags"><span v-for="tag in job.tags">{{tag}} </span></p>
            </div>
            <div class="card-action">
              <a :href="job.link">{{job.source}}</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SearchResults",
  data() {
    return {
      result: null,
      rendered: null
    };
  },
  methods: {
    displayResult: function() {
      this.rendered = []//this.result.data.results[0].result;
      this.result.data.results.forEach(element => {
        element.result.forEach(res => {
          res.source = element.source;
          this.rendered.push(res);
        });
      });
    }
  },
  mounted: function () {
    this.$root.$on('search', (result) => {
      this.result = result;
      this.displayResult();
    });
  }
};
</script>

<style scoped>
.card-content {
  height: 200px;
  overflow-y: hidden;
}

.tags {
  font-weight: bold;
  font-family: monospace;
  padding-top: 20px;
}
</style>
