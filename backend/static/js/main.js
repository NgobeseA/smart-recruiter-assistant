const form = document.getElementById("jobForm");
const previewBox = document.getElementById("jobPreview");
const saveBtn = document.getElementById("saveBtn");

// Live preview
form.addEventListener("input", () => {
  const title = form.title?.value || "";
  const company = form.company?.value || "";
  const location = form.location?.value || "";

  const description = document.getElementById("description").value.split('\n').filter(Boolean);
  const responsibilities = document.getElementById("responsibilities").value.split('\n').filter(Boolean);
  const qualifications = document.getElementById("qualifications").value.split('\n').filter(Boolean);

  previewBox.innerHTML = `
    <h5>${title}</h5>
    <p><strong>${company}</strong></p>
    <p class="text-muted">${location}</p>
    <h6>About the Job</h6>
    ${description.map(line => `<p>${line}</p>`).join("")}
    <h6>Responsibilities</h6>
    <ul>${responsibilities.map(r => `<li>${r}</li>`).join("")}</ul>
    <h6>Qualifications</h6>
    <ul>${qualifications.map(q => `<li>${q}</li>`).join("")}</ul>
  `;
});

// Submit job to backend
saveBtn.addEventListener("click", async () => {
  const jobData = {
    title: form.title.value,
    company: form.company.value,
    location: form.location.value,
    job_type: "Full Time",  // Or pull from select input
    industry: form.industry?.value || "Tech",  // Optional field
    description: document.getElementById("description").value,
    responsibilities: document.getElementById("responsibilities").value,
    qualifications: document.getElementById("qualifications").value,
    required_skills: form.required_skills?.value || "",
  };

  try {
    const response = await fetch("http://localhost:8000/api/jobs/create/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(jobData)
    });
    if (response.ok) {
      alert("Job saved and published successfully!");
      form.reset();
      previewBox.innerHTML = "";
    } else {
      alert("Error publishing job.");
    }
  } catch (err) {
    alert("Request failed.");
    console.error(err);
  }
});