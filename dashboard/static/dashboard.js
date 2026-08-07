let previousTotal = null;

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


        let avgRisk = 0;

        if (total > 0) {
            avgRisk = Math.round(
                data.reduce(
                    (sum, i) => sum + i.risk_score,
                    0
                ) / total
            );
        }


        document.getElementById("totalIncidents").textContent = total;
        document.getElementById("criticalCount").textContent = critical;
        document.getElementById("highCount").textContent = high;
        document.getElementById("mediumCount").textContent = medium;
        document.getElementById("avgRisk").textContent = avgRisk;


        if (previousTotal !== null && total > previousTotal) {

            const alertBox = document.getElementById("liveAlert");

            if (alertBox) {

                alertBox.style.display = "block";

                setTimeout(() => {
                    alertBox.style.display = "none";
                }, 5000);

            }
        }


        previousTotal = total;


    } catch(error) {

        console.error(
            "Dashboard update error:",
            error
        );

    }

}


setInterval(updateDashboard, 5000);

updateDashboard();
