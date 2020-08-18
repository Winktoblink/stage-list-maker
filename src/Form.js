import React from "react";
import Switch from "react-switch";

export default class Form extends React.Component {
  constructor() {
    super();
    this.state = {
        hasWalkOffs: true,
        hasCeiling: true,
        hasWallInfinite: true,
        hasRandom: true,
        hasWater: true,
        hasSymmetry: true,
        hasTransform: true,
        has2D: true,
        hasIce: true,
        hasHurt: true
    };
    this.handleChange = this.handleChange.bind(this);
  }


  handleChange = (name, e) => {
    console.log(e)
    console.log(name)
    this.setState({
      [name]: e
    });
    //this.setState({ hasWalkOffs });
  }

  onSubmit = e => {
    e.preventDefault();
    // this.props.onSubmit(this.state);
    this.setState(this.state);
    this.props.onChange(this.state);
  };

  render() {
    return (
      <form>
        <label>
          <span>Walk Offs</span>
          <Switch
            checked={this.state.hasWalkOffs}
            onChange={e => this.handleChange("hasWalkOffs", e)}
            onColor="#86d3ff"
            onHandleColor="#2693e6"
            handleDiameter={15}
            uncheckedIcon={false}
            checkedIcon={false}
            boxShadow="0px 1px 5px rgba(0, 0, 0, 0.6)"
            activeBoxShadow="0px 0px 1px 10px rgba(0, 0, 0, 0.2)"
            height={10}
            width={24}
            className="react-switch"
            id="material-switch"
          />
        </label>
        <br />
        <label>
          <span>Ceilings</span>
          <Switch
            checked={this.state.hasCeiling}
            onChange={e => this.handleChange("hasCeiling", e)}
            onColor="#86d3ff"
            onHandleColor="#2693e6"
            handleDiameter={15}
            uncheckedIcon={false}
            checkedIcon={false}
            boxShadow="0px 1px 5px rgba(0, 0, 0, 0.6)"
            activeBoxShadow="0px 0px 1px 10px rgba(0, 0, 0, 0.2)"
            height={10}
            width={24}
            className="react-switch"
            id="material-switch"
          />
        </label>
        <br />
        <button onClick={e => this.onSubmit(e)}>Submit</button>
      </form>
    );
  }
}
