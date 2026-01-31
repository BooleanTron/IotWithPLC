async function updateValues() {
  const res = await fetch("/api/values");
  const data = await res.json();

  let varInt = "--";
  let varFloat = "--";

  data.forEach(row => {
    if (row.variable_name === "VarInt") {
      varInt = row.value;
    }
    if (row.variable_name === "VarFloat") {
      varFloat = row.value;
    }
  });

  document.getElementById("varIntValue").innerText = varInt;
  document.getElementById("varFloatValue").innerText = varFloat;
}

setInterval(updateValues, 1000);
updateValues();

document.getElementById("writeForm").addEventListener("submit", async e => {
  e.preventDefault();

  const VarInt = document.getElementById("writeInt").value;
  const VarFloat = document.getElementById("writeFloat").value;

  await fetch("/api/write", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ VarInt, VarFloat })
  });

  document.getElementById("writeInt").value = "";
  document.getElementById("writeFloat").value = "";
});
