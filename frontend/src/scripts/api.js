import axios from "axios";

export function getWaypointPage(currentPage, limit) {
          const params = new URLSearchParams(); // todo clean up
          const offset = (currentPage-1)*limit;
          params.append('offset', offset || 0);
          params.append('limit', limit);
          return axios.get("http://localhost:8000/waypoints", {
            params: params
          })
}

export function createWaypoint(latitude, longitude) {
    return axios.post("http://localhost:8000/waypoints", { latitude , longitude });
}