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

  handleChange(event) {
  	let val = event.target.value;
  	this.setState({
      'request': val,
      //'submitted': false
    });
  }

  handleSubmit(event) {
    event.preventDefault();
    alert('You submitted: ' + this.state.request);
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
	    console.log(response);
      this.setState({'response': response.body});
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

  renderUserInfo() {
    return (
      <div>
        {this.state.response}
      </div>
    );
  }

  render () {
  	return (
	    <div className="App">
	      <form onSubmit={this.handleSubmit}>
	      	<label>
		        How can we help you?
		        <input type="text" placeholder="What years was the bmw 3 series sold" value={this.state.request} onChange={this.handleChange}/>
	      	</label>
	      	<input type="submit" value="Submit" />
	      </form>
        {this.state.submitted && this.renderUserInfo()}
        <div className="response"></div>
	    </div>
	  );
  }
}

export default WitForm;
