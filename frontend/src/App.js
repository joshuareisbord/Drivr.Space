import React from 'react';
import './App.css';
import Amplify, { API } from 'aws-amplify';

Amplify.configure({
    // OPTIONAL - if your API requires authentication 
    Auth: {
        // REQUIRED - Amazon Cognito Identity Pool ID
        identityPoolId: 'us-west-2:cfecc65c-67fd-45b1-b461-7f3c60a32c4b',
        // REQUIRED - Amazon Cognito Region
        region: 'us-west-2', 
        // OPTIONAL - Amazon Cognito User Pool ID
        //userPoolId: 'XX-XXXX-X_abcd1234', 
        // OPTIONAL - Amazon Cognito Web Client ID (26-char alphanumeric string)
        //userPoolWebClientId: 'a1b2c3d4e5f6g7h8i9j0k1l2m3',
    },
    API: {
        endpoints: [
            {
                name: "carAPI",
                endpoint: "https://25b7pfuop1.execute-api.us-west-1.amazonaws.com/prod"
            }
        ]
    }
});

class WitForm extends React.Component {
	constructor(props) {
    super(props);
    this.state = {
      'request': '',
      'response': '',
      'submitted': false
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  componentDidMount(){
    document.title = "Drivr"
  }

  handleChange(event) {
  	let val = event.target.value;
  	this.setState({
      'request': val,
      //'submitted': false
    });
  }

  handleSubmit(event) {
    event.preventDefault();
    const apiName = 'carAPI'; 
  	const path = '/getyears';
  	const myInit = {
  	    body: JSON.stringify({'body': this.state.request}),
  	    headers: {
  	    	"Access-Control-Allow-Origin" : "http://localhost:3000", // Required for CORS support to work
      		"Access-Control-Allow-Credentials" : "true", // Required for cookies, authorization headers with HTTPS
  	    }
  	};

  	API
  	  .post(apiName, path, myInit)
  	  .then(response => {
        this.setState({'response': response.body.entries}, console.log(response));
  	  })
  	  .catch(error => {
  	    console.log(error.message);
  	});

    this.setState({
      'submitted': false
    });

    this.setState({
      'request': '',
      'submitted': true
    });
  }

  carItems(props) {
    return (
      <div>year: {props.value.year}</div>
    );
  }
  // <React.Fragment>
  //       <div>
  //         year: {car[0]["year"]}
  //       </div>
  //       <div>
  //         make: {car[0]["make"]}
  //       </div>
  //       <div>
  //         model: {car[0]["model"]}
  //       </div>
  //     </React.Fragment>
  renderUserInfo() {
    const cars = this.state.response;
    console.log("Response:" + this.state.response);
    if (cars) {
      const listCars = cars.map((car) =>
        <div className="carInfo">
          <div>
            year: {car[0].year}
          </div>
          <div>
            make: {car[0].make}
          </div>
          <div>
            model: {car[0].model}
          </div>
          <div>
            mpg: {car[0].mpg}
          </div>
          <div>
            cylinders: {car[0].cylinders}
          </div>
          <div>
            displacement: {car[0].displacement}
          </div>
          <div>
            drive: {car[0].drive}
          </div>
          <div>
            drive: {car[0].drive}
          </div>
          <div>
            fuel grade: {car[0].fuel_grade}
          </div>
          <div>
            vehicle class: {car[0].vehicle_class}
          </div>
          <div>
            transmission: {car[0].transmission}
          </div>
        </div>
      );
      return (
        listCars
      );
    }
    return <div></div>
  }

  render () {
  	return (
	    <div className="App">
        <div className="body">
          <div className="title">
            DRIVR.SPACE
          </div>
  	      <form onSubmit={this.handleSubmit}>
  	      	<label className="question">
              Ask us a question: 
            </label>
            <label className="questionInput"> 
  		        <input type="text" placeholder="Porsche 911 fuel economy" value={this.state.request} onChange={this.handleChange}/>
  	      	</label>
  	      	<input type="submit" value="Submit" />
  	      </form>
          {this.state.submitted && this.renderUserInfo()}
        </div>
        <footer className="footer">
          Created By Josh Reisbord and Ryan Jacobs for Borderhacks 2020
        </footer>
	    </div>
	  );
  }
}

export default WitForm;
