<template>
  <div id="app">
    <b-container>
      <b-row>
        <b-jumbotron header="Waypoint Full Stack Demo"></b-jumbotron>
      </b-row>
      <b-form-row>
        <b-col>
          <waypoint-form />
        </b-col>
      </b-form-row>
      <b-row>
        <b-col>
        <waypoint-list />
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import WaypointForm from "./components/WaypointForm.vue";
import WaypointList from "./components/WaypointList.vue";

export default {
  name: "App",
  components: {
    WaypointForm,
    WaypointList,
  },
};
</script>

<style>
</style>
