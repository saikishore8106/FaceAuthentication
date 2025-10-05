import React, { useState } from "react";

function App() {
  const [capturedImage, setCapturedImage] = useState(null);
  const [authImage, setAuthImage] = useState(null);
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const authenticateFace = async () => {
    setLoading(true);
    setResult("");
    try {
      const response = await fetch("http://127.0.0.1:8000/authenticate");
      const data = await response.json();

      if (data.captured_image) {
        const capturedFilename = data.captured_image.split("\\").pop();
        setCapturedImage(`http://127.0.0.1:8000/captured/${capturedFilename}`);
      }

      if (data.auth_image) {
        const authFilename = data.auth_image.split("\\").pop();
        setAuthImage(`http://127.0.0.1:8000/known_faces/${authFilename}`);
      } else {
        setAuthImage(null);
      }

      if (data.success) {
        setResult(`Authenticated as: ${data.authenticated_as}`);
      } else {
        setResult(`Authentication failed. ${data.message || ""}`);
      }

    } catch (err) {
      setResult(`Failed: ${err}`);
      setCapturedImage(null);
      setAuthImage(null);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>Face Authentication</h1>
      <button style={styles.button} onClick={authenticateFace} disabled={loading}>
        {loading ? "Processing..." : "Authenticate"}
      </button>

      {result && <p style={styles.result}>{result}</p>}

      <div style={styles.imagesContainer}>
        {capturedImage && (
          <div style={styles.imageBox}>
            <h3>Captured Image</h3>
            <img src={capturedImage} alt="Captured" style={styles.image} />
          </div>
        )}

        {authImage && (
          <div style={styles.imageBox}>
            <h3>Matched Image</h3>
            <img src={authImage} alt="Matched" style={styles.image} />
          </div>
        )}
      </div>
    </div>
  );
}

const styles = {
  container: {
    fontFamily: "Arial, sans-serif",
    maxWidth: "800px",
    margin: "50px auto",
    textAlign: "center",
    padding: "20px",
    borderRadius: "10px",
    boxShadow: "0 4px 15px rgba(0,0,0,0.2)",
  },
  title: {
    color: "#333",
  },
  button: {
    padding: "10px 20px",
    fontSize: "16px",
    margin: "20px 0",
    borderRadius: "5px",
    cursor: "pointer",
    backgroundColor: "#4CAF50",
    color: "#fff",
    border: "none",
  },
  result: {
    fontSize: "18px",
    margin: "20px 0",
    fontWeight: "bold",
  },
  imagesContainer: {
    display: "flex",
    justifyContent: "center",
    gap: "40px", // space between images
    flexWrap: "wrap",
    marginTop: "20px",
  },
  imageBox: {
    textAlign: "center",
  },
  image: {
    width: "300px", // same width
    height: "300px", // same height
    objectFit: "cover", // maintains aspect ratio and crops if necessary
    borderRadius: "10px",
    boxShadow: "0 4px 10px rgba(0,0,0,0.2)",
  },
};

export default App;
