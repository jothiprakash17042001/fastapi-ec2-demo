document.addEventListener("DOMContentLoaded", () => {
    const startBtn = document.getElementById("startBtn");
    const stopBtn = document.getElementById("stopBtn");
    const statusMessage = document.getElementById("statusMessage");
    const statusText = document.getElementById("statusText");

    // Load initial info
    fetch("/info")
        .then(res => res.json())
        .then(data => {
            document.getElementById("awsRegion").innerText = data.aws_region || "N/A";
            document.getElementById("startLambda").innerText = data.start_lambda || "N/A";
            document.getElementById("stopLambda").innerText = data.stop_lambda || "N/A";
        })
        .catch(err => console.error("Error fetching info:", err));

    const setStatus = (message, type) => {
        statusMessage.classList.remove("hidden", "success", "error");
        statusMessage.style.display = "block";
        if (type) {
            statusMessage.classList.add(type);
        }
        statusText.innerText = message;
    };

    const disableButtons = (disabled) => {
        startBtn.disabled = disabled;
        stopBtn.disabled = disabled;
    };

    const triggerAction = async (endpoint, actionName) => {
        disableButtons(true);
        setStatus(`${actionName}ing server...`, "");
        
        try {
            const response = await fetch(endpoint, {
                method: "POST"
            });
            const data = await response.json();
            
            if (response.ok && data.status === "success") {
                setStatus(`Successfully triggered ${actionName}!`, "success");
            } else {
                setStatus(`Error: ${data.detail || 'Unknown error'}`, "error");
            }
        } catch (error) {
            setStatus(`Network error: ${error.message}`, "error");
        } finally {
            disableButtons(false);
        }
    };

    startBtn.addEventListener("click", () => triggerAction("/start-server", "Start"));
    stopBtn.addEventListener("click", () => triggerAction("/stop-server", "Stop"));
});
