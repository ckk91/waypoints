<template>
  <b-card>
    <b-alert variant="danger" v-model="errorAlert" dismissible>{{
      errMsg
    }}</b-alert>
    <b-alert variant="success" v-model="successAlert" dismissible
      >Successfully added waypoint number {{ resultId }}</b-alert
    >

    <b-form @submit="onSubmit">
      <label for="wp-input">
        Enter Waypoint Coordinate (Latitude, Longitude)
      </label>
      <b-form-input
        id="wp-input"
        placeholder="41.40338, 2.17403"
        class="mb-2"
        v-model="form.waypoint"
        required
      />
      <b-button type="submit" variant="primary" class="mr-3">Save</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>
  </b-card>
</template>
<script>
import { getWaypointPage, createWaypoint } from "../scripts/api.js";
import { parseWaypoint } from "../scripts/util.js";
export default {
  name: "WaypointForm",
  data() {
    return {
      errorAlert: false,
      successAlert: false,
      errMsg: "",
      resultId: 0,
      form: {
        waypoint: "",
      },
    };
  },
  methods: {
    waypointError() {
      this.errorAlert = true;
      this.errMsg =
        "Latitude must be between -85.0 and 85.05115; Longitude between -180.0 and 180.0";
    },
    onSubmit(e) {
      e.preventDefault();

      const res = parseWaypoint(this.form.waypoint);
      if (res === null) {
        this.waypointError();
        return;
      }

      const { lat, lon } = res;

      createWaypoint(lat, lon)
        .then((res) => {
          if (res.status == 201) {
            this.successAlert = true;
            this.resultId = res.data.id;

            getWaypointPage(
              this.$store.state.wpTable.currentPage,
              this.$store.state.wpTable.itemsPerPage
            ).then((res) => {
              this.$store.commit("updateRows", res.data.total);
              this.$store.commit("updateWaypoints", res.data.values);
            });
          }
        })
        .catch((err) => {
          if (err.response.status == 422) {
            this.waypointError();
          } else {
            this.errorAlert = true;
            this.errMsg = err.message;
          }
        });
    },
  },
};
</script>