import logo from './logo.svg';
import './App.css';
import embedToDashboard from './awsConfig'
embedToDashboard()
function App() {
  
  return (
    <div className="App">
      <h1>ETL Pipeline-Dashboard</h1>
      <iframe
        width="960"
        height="720"
        src="https://eu-west-1.quicksight.aws.amazon.com/sn/embed/share/accounts/346953440318/dashboards/cf94f283-b027-4dae-8dbe-1da05926670f?directory_alias=akaash12345">
    </iframe>
    </div>
  );
}

export default App;
