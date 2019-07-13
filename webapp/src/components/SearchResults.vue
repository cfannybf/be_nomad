<template>
  <div class="searchresults" v-if="rendered">
    <div class="container" id="search_result">
      <div class="row">
        <h5 class="center">Search results</h5>
      </div>

      <div class="row" v-for="job in rendered">
        <div class="container">
          <h4>
            <a :href="job.link">{{job.company}}</a>
          </h4>
          <p class="job-result">{{job.title}}</p>
          <p class="tags job-result">
            <span v-for="tag in job.tags">{{tag}}</span>
          </p>
          <p class="job-result">
            <a class="job-link" :href="job.link">{{job.link}}</a>
          </p>
          <br />
        </div>
      </div>

      <div class="container" v-if="pages">
        <ul class="pagination">
          <li class="waves-effect" v-on:click="movePage(-1)">
            <a href="#search_result">
              <i class="material-icons">chevron_left</i>
            </a>
          </li>
          <li
            class="waves-effect"
            v-for="pageNum in pages.length"
            v-bind:class="{'active': currentPage == pageNum}"
          >
            <a href="#search_result" v-on:click="displayPage(pageNum)">{{pageNum}}</a>
          </li>
          <li class="waves-effect" v-on:click="movePage(1)">
            <a href="#search_result">
              <i class="material-icons">chevron_right</i>
            </a>
          </li>
        </ul>
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
      rendered: null,
      pages: null,
      currentPage: null
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
      this.paginate();
    },
    paginate: function() {
      if (this.rendered.length > 10) {
        this.pages = [[]];
        var currentPage = 0;
        var counter = 0;
        this.rendered.forEach(el => {
          if (counter == 10) {
            this.pages.push([]);
            currentPage += 1;
            counter = 0;
          }
          this.pages[currentPage].push(el);
          counter += 1;
        });

        this.displayPage(1);
      }
    },
    displayPage: function(i) {
      this.currentPage = i;
      i = i - 1;
      this.rendered = this.pages[i];
    },
    movePage: function(k) {
      if (
        (k > 0 && this.currentPage === this.pages.length) ||
        (k < 0 && this.currentPage == 1)
      ) {
        return;
      }
      this.currentPage += k;
      this.displayPage(this.currentPage);
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
      this.pages = null;
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

li.active {
  background-color: #01579b !important;
}
</style>
