<template>
  <div class="navbar">
    <nav role="navigation">
      <div id="nav-mobile" class="nav-wrapper container">
        <a id="logo-container" href="#" class="brand-logo">be nomad</a>
        <ul class="right hide-on-med-and-down">
          <li>
            <a href="#">Home</a>
          </li>
          <li>
            <a href="#">FAQ</a>
          </li>
          <li>
            <a href="#">About us</a>
          </li>
          <li>
            <a href="#">Report bug</a>
          </li>
        </ul>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  name: "NavBar"
};
</script>

<style scoped>
nav {
  background-color: transparent;
  box-shadow: none;
}
</style>