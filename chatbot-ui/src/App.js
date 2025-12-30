import React, { useEffect, useState } from "react";
import axios from "axios";

/**
 * ✅ BACKEND API (LOCAL ONLY)
 * Backend runs on localhost:8001
 * DO NOT use ngrok here
 */
const API = process.env.REACT_APP_API_BASE_URL;

function App() {
  const [csam, setCsam] = useState(null);
  const [customerIndex, setCustomerIndex] = useState(0);
  const [step, setStep] = useState("WELCOME"); // WELCOME | OVERVIEW | ENHANCE | UPDATE | DONE
  const [theme, setTheme] = useState("light"); // ✅ DEFAULT LIGHT MODE
  const [formData, setFormData] = useState({});

  /* ===============================
     LOAD DATA (WORKS FOR MULTIPLE CSAMs)
  =============================== */
  useEffect(() => {
    axios
      .get(`${API}/get_data`)
      .then((res) => {
        const csamObj = res.data[0].csam; // future-ready
        setCsam(csamObj);
        setFormData(csamObj.customers[0]);
      })
      .catch((err) => {
        console.error("Backend not reachable", err);
      });
  }, []);

  if (!csam) {
    return (
      <div style={{ padding: 40 }}>
        <h3>Loading Customer Intelligence...</h3>
      </div>
    );
  }

  const customer = csam.customers[customerIndex];

  /* ===============================
     NAVIGATION
  =============================== */
  const nextCustomer = () => {
    const next = customerIndex + 1;
    if (next < csam.customers.length) {
      setCustomerIndex(next);
      setFormData(csam.customers[next]);
      setStep("OVERVIEW");
    } else {
      setStep("DONE");
    }
  };

  const saveUpdate = async () => {
    try {
      await axios.post(`${API}/update_customer`, {
        csamId: csam.csamId,
        customerName: customer.customerName,
        updatedData: JSON.parse(JSON.stringify(formData))
      });
      nextCustomer();
    } catch (err) {
      alert("Failed to save update");
      console.error(err);
    }
  };

  /* ===============================
     UI
  =============================== */
  return (
    <div style={page(theme)}>
      <header style={header}>
        <h1>AED C-IQ Customer Intelligence</h1>
        <p>CSAM → Customer → Validate & Update Mission-Critical Information</p>

        <button
          style={toggleBtn}
          onClick={() => setTheme(theme === "light" ? "dark" : "light")}
        >
          {theme === "light" ? "🌙 Dark" : "☀️ Light"}
        </button>
      </header>

      <div style={container}>

        {/* ================= WELCOME ================= */}
        {step === "WELCOME" && (
          <Card theme={theme}>
            <h3>Hi {csam.csamName},</h3>
            <p>
              Welcome to <b>Mission Critical Services for Azure Platform</b>.
              <br /><br />
              Please take a few minutes to validate and update mission-critical
              customer information to ensure accuracy and readiness.
            </p>
            <button style={primaryBtn} onClick={() => setStep("OVERVIEW")}>
              Start Validation
            </button>
          </Card>
        )}

        {/* ================= OVERVIEW ================= */}
        {step === "OVERVIEW" && (
          <Card theme={theme}>
            <h3>Customer Overview</h3>
            <Info label="Customer Name" value={customer.customerName} />
            <Info label="TP ID" value={customer.tpId} />
            <Info label="Industry" value={customer.industryBusinessSegment} />
            <Info label="Region" value={customer.regionAssociatedWithTPID} />

            <div style={{ marginTop: 20 }}>
              <button style={successBtn} onClick={nextCustomer}>
                Correct
              </button>
              <button
                style={secondaryBtn}
                onClick={() => setStep("ENHANCE")}
              >
                Enhance
              </button>
              <button
                style={warningBtn}
                onClick={() => setStep("UPDATE")}
              >
                Update
              </button>
            </div>
          </Card>
        )}

        {/* ================= ENHANCE ================= */}
        {step === "ENHANCE" && (
          <Card theme={theme}>
            <h3>Customer Details (Read-Only)</h3>
            {Object.entries(customer).map(([k, v]) => (
              <pre key={k} style={pre(theme)}>
                <b>{k}</b>: {JSON.stringify(v, null, 2)}
              </pre>
            ))}
            <button style={secondaryBtn} onClick={() => setStep("OVERVIEW")}>
              Back
            </button>
          </Card>
        )}

        {/* ================= UPDATE ================= */}
        {step === "UPDATE" && (
          <Card theme={theme}>
            <h3>Edit Customer</h3>

            {Object.entries(formData).map(([key, value]) => (
              <div key={key} style={{ marginBottom: 14 }}>
                <label><b>{key}</b></label>
                <textarea
                  style={input(theme)}
                  value={JSON.stringify(value, null, 2)}
                  onChange={(e) =>
                    setFormData({
                      ...formData,
                      [key]: JSON.parse(e.target.value || "{}")
                    })
                  }
                />
              </div>
            ))}

            <div style={{ marginTop: 20 }}>
              <button
                style={secondaryBtn}
                onClick={() => setStep("OVERVIEW")}
              >
                Back
              </button>
              <button style={primaryBtn} onClick={saveUpdate}>
                Save & Continue
              </button>
            </div>
          </Card>
        )}

        {/* ================= DONE ================= */}
        {step === "DONE" && (
          <Card theme={theme}>
            <h3>✅ Completed</h3>
            <p>All customers for this CSAM have been validated.</p>
          </Card>
        )}
      </div>
    </div>
  );
}

/* ================= STYLES ================= */

const page = (theme) => ({
  minHeight: "100vh",
  background: theme === "dark" ? "#0b0b0b" : "#f8fafc",
  color: theme === "dark" ? "#ffffff" : "#111827",
  padding: 40
});

const header = { textAlign: "center", position: "relative" };
const toggleBtn = { position: "absolute", right: 0, top: 0 };
const container = { maxWidth: 900, margin: "auto" };

const Card = ({ children, theme }) => (
  <div
    style={{
      background: theme === "dark" ? "#161616" : "#ffffff",
      padding: 32,
      borderRadius: 20,
      marginBottom: 24,
      boxShadow:
        theme === "dark"
          ? "0 10px 30px rgba(0,0,0,0.6)"
          : "0 10px 30px rgba(0,0,0,0.1)"
    }}
  >
    {children}
  </div>
);

const Info = ({ label, value }) => (
  <p><b>{label}:</b> {value}</p>
);

const input = (theme) => ({
  width: "100%",
  padding: 10,
  borderRadius: 8,
  background: theme === "dark" ? "#0f0f0f" : "#ffffff",
  color: theme === "dark" ? "#ffffff" : "#000000",
  border: "1px solid #ccc"
});

const pre = (theme) => ({
  background: theme === "dark" ? "#0f0f0f" : "#f1f5f9",
  color: theme === "dark" ? "#ffffff" : "#000000",
  padding: 12,
  borderRadius: 10,
  marginBottom: 10,
  overflowX: "auto"
});

const primaryBtn = {
  padding: 12,
  background: "#2563eb",
  color: "#fff",
  borderRadius: 10
};
const successBtn = { ...primaryBtn, background: "#16a34a", marginRight: 10 };
const warningBtn = { ...primaryBtn, background: "#f59e0b", marginLeft: 10 };
const secondaryBtn = { ...primaryBtn, background: "#6b7280", marginLeft: 10 };

export default App;
