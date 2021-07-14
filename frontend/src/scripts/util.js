export function parseWaypoint(waypoint) {
        const res = waypoint.match(/^(-?\d+(?:\.\d+)?),? +(-?\d+(?:\.\d+)?)$/);
        
        if (res === null || res.length !== 3){
                return null;
        }
        
        const lat = parseFloat(res[1]);
        const lon = parseFloat(res[2]);

        return {lat, lon};
}