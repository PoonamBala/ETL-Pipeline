import { embedSession ,embedDashboard} from 'amazon-quicksight-embedding-sdk';
const onDashboardLoad = ()=>{
    console.log("hello")
}
const onError= ()=>{
    console.log("error")
}
function embedToDashboard() {
    var containerDiv = document.getElementById("container");
    var options = {
        url: "https://cloudwatch.amazonaws.com/dashboard.html?dashboard=Cloudwatch_metrics&context=eyJSIjoidXMtZWFzdC0xIiwiRCI6ImN3LWRiLTM0Njk1MzQ0MDMxOCIsIlUiOiJ1cy1lYXN0LTFfQTFTUUlVOUx0IiwiQyI6IjQ0OTQzanRxZGhsMWE3cHNiMzJ2dmZobTloIiwiSSI6InVzLWVhc3QtMTowNWE5MGQ2Yy0xZDdmLTQxNDEtODk0NS1iMDRjMTUzYWYwOWIiLCJNIjoiUHVibGljIn0=",
        container: containerDiv,
        parameters: {
            country: 'United States'
        },
        scrolling: "no",
        height: "700px",
        width: "1000px"
    };
    
    const dashboard = embedDashboard(options);
    dashboard.on('error', onError);
    dashboard.on('load', onDashboardLoad);
}
export default embedToDashboard