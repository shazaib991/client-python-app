import axios from "axios";
import { useEffect } from "react";
import { useState } from "react";

function App() {
  const [acceptCookie, setAcceptCookie] = useState(
    document.cookie.includes("status=accepted") ? "accepted" : "not accepted"
  );
  const [data, setData] = useState([]);
  const [userIp, setUserIp] = useState("");

  const language = window.navigator.language || window.navigator.userLanguage;
  let device = "";
  let browserName = "";
  let dimentions = `${window.innerWidth}x${window.innerHeight}`;

  const getIpAddress = async () => {
    try {
      const response = await axios.get("https://api.ipify.org?format=json");
      const userIp = response.data;
      setUserIp(userIp.ip);
    } catch (err) {
      setUserIp("could not get ip address");
      console.log(err);
    }
  };

  const getData = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:5000/test");
      const data = response.data;

      setData(data);
    } catch (err) {
      console.log(err);
    }
  };

  useEffect(() => {
    getIpAddress();
  }, []);

  //using media query to check mobile or desktop
  if (window.matchMedia("(max-width: 767px)").matches) {
    device = "mobile or tablet";
  } else {
    device = "desktop or laptop";
  }

  //using navigator to check browser version
  if (window.navigator.userAgent.includes("Firefox/")) {
    browserName = "firefox";
  } else if (window.navigator.userAgent.includes("Edg/")) {
    browserName = "edge";
  } else if (window.navigator.userAgent.includes("Chrome/")) {
    browserName = "chrome";
  } else if (window.navigator.userAgent.includes("Safari/")) {
    browserName = "safari";
  }

  const setCookie = () => {
    document.cookie = "status=accepted";
    setAcceptCookie("accepted");
  };

  return (
    <>
      <div className="App">
        <h1>language: {language}</h1>
        <h1>device: {device}</h1>
        <h1>brower name: {browserName}</h1>
        <h1>browser dimentions: {dimentions}</h1>
        <h1>ip address: {userIp}</h1>
        <h1>cookie status: {acceptCookie}</h1>
      </div>
      {acceptCookie !== "accepted" ? (
        <div>
          <h1>cookies</h1>
          <button onClick={setCookie}>accept</button>
        </div>
      ) : (
        ""
      )}
      <div>
        <button onClick={getData}>show stored data</button>
        {data.length !== 0 ? (
          <table>
            <tr>
              <th>language</th>
              <th>device</th>
              <th>browser name</th>
              <th>browser dimentions</th>
              <th>ip address</th>
              <th>cookie status</th>
            </tr>
            {data.map((item, index) => {
              return (
                <tr key={index}>
                  <td>{item.language}</td>
                  <td>{item.device}</td>
                  <td>{item.browserName}</td>
                  <td>{item.browserDimentions}</td>
                  <td>{item.ipAddress}</td>
                  <td>{item.cookieStatus}</td>
                </tr>
              );
            })}
          </table>
        ) : (
          ""
        )}
      </div>
    </>
  );
}

export default App;
