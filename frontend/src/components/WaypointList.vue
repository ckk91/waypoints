<template>
  <b-card class="mt-3">
    <b-pagination
      v-model="currentPage"
      :total-rows="totalRows"
      :per-page="perPage"
      aria-controls="waypointTable"
      @input="onPaginationInput"
    ></b-pagination>
    <b-table
      id="waypointTable"
      :total-rows="totalRows"
      :items="items"
      :current-page="currentPage"
      :fields="fields"
      striped
      hover
      small
    >
    </b-table>
  </b-card>
</template>

<script>
import { getWaypointPage } from "../scripts/api.js";
export default {
  name: "WaypointList",
  data() {
    return {
      fields: ["id", "latitude", "longitude"],
    };
  },
  computed: {
    items() {
      return this.$store.state.waypoints;
    },
    totalRows() {
      return this.$store.state.wpTable.totalRows;
    },
    currentPage: {
      get() {
        return this.$store.state.wpTable.currentPage;
      },
      set(page) {
        this.$store.commit("updateTablePage", page);
      },
    },
    perPage() {
      return this.$store.state.wpTable.itemsPerPage;
    },
  },
  methods: {
    onPaginationInput() {
      getWaypointPage(
        this.$store.state.wpTable.currentPage,
        this.$store.state.wpTable.itemsPerPage
      ).then((res) => {
        this.$store.commit("updateRows", res.data.total);
        this.$store.commit("updateWaypoints", res.data.values);
      });
    },
  },
  mounted() {
    getWaypointPage(
      this.$store.state.wpTable.currentPage,
      this.$store.state.wpTable.itemsPerPage
    ).then((res) => {
      this.$store.commit("updateRows", res.data.total);
      this.$store.commit("updateWaypoints", res.data.values);
    });
  },
};
</script>