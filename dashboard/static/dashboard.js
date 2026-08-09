let previousIncidentIds = null;

async function updateDashboard() {

    try {

        const response = await fetch("/api/incidents");
        const result = await response.json();

        const data = result.data || result;

        const total = data.length;

        const critical = data.filter(
            i => i.severity === "CRITICAL"
        ).length;

        const high = data.filter(
            i => i.severity === "HIGH"
        ).length;

        const medium = data.filter(
            i => i.severity === "MEDIUM"
        ).length;

        const low = data.filter(
            i => i.severity === "LOW"
        ).length;


        let avgRisk = 0;

        if (total > 0) {

            avgRisk = Math.round(
                data.reduce(
                    (sum, i) => sum + Number(i.risk_score || 0),
                    0
                ) / total
            );

        }


        document.getElementById("totalIncidents").textContent = total;
        document.getElementById("criticalCount").textContent = critical;
        document.getElementById("highCount").textContent = high;
        document.getElementById("mediumCount").textContent = medium;
        document.getElementById("avgRisk").textContent = avgRisk;


        /*
         * Real-Time SOC Alert
         */

        const currentIds = data.map(
            incident => incident.id
        );

        if (previousIncidentIds !== null) {

            const newIncidents = data.filter(
                incident =>
                    !previousIncidentIds.includes(incident.id)
            );


            const criticalIncidents = newIncidents.filter(
                incident => incident.severity === "CRITICAL"
            );

            if (criticalIncidents.length > 0) {

                const incident = criticalIncidents[0];

                const alertBox =
                    document.getElementById("liveAlert");


                if (alertBox) {

                    alertBox.innerHTML = `
                        🚨 <strong>CRITICAL SECURITY ALERT</strong>
                        <br>
                        Incident: ${incident.incident}
                        <br>
                        Severity: ${incident.severity}
                        <br>
                        Source IP: ${incident.source_ip || "Unknown"}
                        <br>
                        Risk Score: ${incident.risk_score}
                    `;

                    alertBox.style.display = "block";


                    setTimeout(() => {

                        alertBox.style.display = "none";

                    }, 8000);

                }

            }

        }


        previousIncidentIds = currentIds;


    } catch (error) {

        console.error(
            "Dashboard update error:",
            error
        );

    }

}


setInterval(updateDashboard, 5000);

updateDashboard();
