const BASE_URL = "https://resume-analyzer-0tc9.onrender.com";

// Navigate
function goTo(page) {
    window.location.href = page;
}

// Save token
function saveToken(token) {
    localStorage.setItem("token", token);
}

// Get token
function getToken() {
    return localStorage.getItem("token");
}

// Register
async function register() {
    const username = document.getElementById("reg-username").value;
    const email = document.getElementById("reg-email").value;
    const password = document.getElementById("reg-password").value;

    try {
        const res = await fetch(`${BASE_URL}/api/auth/register/`, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({username, email, password})
        });

        const data = await res.json();

        if (res.status === 201) {
            alert("Registered successfully!");
            window.location.href = "login.html";
        } else {
            alert(JSON.stringify(data));
        }

    }catch (error) {
        console.error(error);
        alert("Network or CORS error");
    }
}
// Login
async function login() {
    const username = document.getElementById("login-username").value;
    const password = document.getElementById("login-password").value;

    const res = await fetch(`${BASE_URL}/api/auth/login/`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({username, password})
    });

    const data = await res.json();

    saveToken(data.access);

    alert("Login successful!");
    window.location.href = "index.html";
}

// Upload + Analyze
let resumeId = "";

async function analyze() {
    const token = getToken();
    if (!token) {
        alert("Please login first!");
        window.location.href = "login.html";
        return;
    }
    const file = document.getElementById("resume-file").files[0];

    const formData = new FormData();
    formData.append("file", file);

    const uploadRes = await fetch(`${BASE_URL}/api/resumes/upload/`, {
        method: "POST",
        headers: {
            "Authorization": `Bearer ${token}`
        },
        body: formData
    });

    const uploadData = await uploadRes.json();
    resumeId = uploadData.id;

    const job_description = document.getElementById("job-desc").value;

    const res = await fetch(`${BASE_URL}/api/analysis/analyze/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`
        },
        body: JSON.stringify({
            resume_id: resumeId,
            job_description
        })
    });

    const data = await res.json();

    document.getElementById("result").innerText =
        JSON.stringify(data, null, 2);
}