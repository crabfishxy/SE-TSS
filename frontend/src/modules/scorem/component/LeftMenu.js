// React
import React, {Component} from 'react';
// Reducer
import store from "../../../top/stores"
import {changePage} from "../actions";
import {ENTER_SCORE, SEARCH_SCORE_TEA, SEARCH_SCORE_STU, ANALYSIS_SCORE} from "../reducers";
// UI
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import {Menu, MenuItem} from 'material-ui/Menu';
import Divider from 'material-ui/Divider';
import Paper from 'material-ui/Paper';

const style = {
  menu: {
    float: 'left',
  },
  paper: {
    display: 'inline-block',
    margin: '16px 32px 16px 0',
  },
};

class LeftMenu extends Component {
  render() {
    return (
      <MuiThemeProvider>
        <Paper style={style.paper}>
          <Menu desktop={true} style={style}>
            <MenuItem primaryText="返回主页"/>
            <Divider/>
            <MenuItem primaryText="成绩录入" onClick={() => {
              store.dispatch(changePage(ENTER_SCORE))
            }}/>
            <MenuItem primaryText="成绩查询" onClick={() => {
              store.dispatch(changePage(SEARCH_SCORE_TEA))
            }}/>
            <MenuItem primaryText="成绩分析" onClick={() => {
              store.dispatch(changePage(ANALYSIS_SCORE))
            }}/>
          </Menu>
        </Paper>
      </MuiThemeProvider>
    );
  }
}

export default LeftMenu;

/*
import React from 'react';
import Divider from 'material-ui/Divider';
import {Menu, MenuItem} from 'material-ui/Menu';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';

const style = {
  // Without this, the menu overflows the CodeExample container.
  float: 'left',
};

class LeftMenu extends React.Component{ 
    render(){
        return (
            
        );
    }
  
}

export default LeftMenu;
*/