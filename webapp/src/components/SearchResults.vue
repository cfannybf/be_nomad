<template>
  <div class="searchresults" v-if="rendered">
    <div class="container" id="search_result">
      <div class="row">
        <h5 class="center">Search results</h5>
      </div>

      <div class="row" v-for="job in rendered">
        <div class="container">
          <h4><a :href="job.link">{{job.company}}</a></h4>
          <p class="job-result">{{job.title}}</p>
          <p class="tags job-result">
            <span v-for="tag in job.tags">{{tag}} </span>
          </p>
          <p class="job-result"><a class="job-link" :href="job.link">{{job.link}}</a></p>
          <br />
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
      this.rendered = []; //this.result.data.results[0].result;
      this.result.data.results.forEach(element => {
        element.result.forEach(res => {
          res.source = element.source;
          this.rendered.push(res);
        });
      });
    }
  },
  mounted: function() {
    this.$root.$on("search", result => {
      this.result = result;
      this.displayResult();
    });
    this.$root.$on("clear_results", result => {
      this.result = null;
      this.rendered = null;
    });
  }
};
</script>

<style scoped>
.tags {
  font-weight: bold;
  font-family: monospace;
  padding-top: 15px;
}

p.job-result {
  margin: 0px;
  padding: 0px;
}

.job-link {
  color: #9fa8da;
}

h4 {
  margin-bottom: 0px;
}
</style>
