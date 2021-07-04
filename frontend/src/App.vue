<template>
  <div id="app">
    <b-navbar type="light" variant="light" class="mb-3">
      <b-navbar-brand> Waypoint Full Stack Demo W/ Pagination </b-navbar-brand>
    </b-navbar>
    <b-container>
      <b-row>
        <b-col>
          <p>
            Enter waypoint coordinates in the form below. The submitted
            coordinates will be listed in the table further down. <br />
            Use the pagination to view all of them, if applicable.
          </p>
        </b-col>
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
