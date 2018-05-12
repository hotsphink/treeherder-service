import React from 'react';

export const PinBoardContext = React.createContext({
  pinnedJobs: [],
  relatedBugs: [],
  pinJob: () => { console.log("pinJob raw"); },
  addBug: () => { console.log("addBug raw"); },
});

export function withPinBoard(Component) {
  return function PinBoardComponent(props) {
    return (
      <PinBoardContext.Consumer>
        {pinBoard => <Component {...props} pinBoard={pinBoard} />}
      </PinBoardContext.Consumer>
    );
  };
}
