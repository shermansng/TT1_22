import * as React from 'react';
import Button from '@mui/material/Button';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';
import IconButton from '@mui/material/IconButton';
import DeleteIcon from '@mui/icons-material/Delete';

function ConfirmationPopUp() {
  const [open, setOpen] = React.useState(false);
  
  // for initial click of button
  const handleClickOpen = () => {
    setOpen(true);
  };

  // for closing the popup
  const handleClose = () => {
    setOpen(false);
  };

  // for deleting the scheduled transaction and closing the popup
  const handleDelete = () => {
    setOpen(false);
  };

  return (
    <div>
      <IconButton onClick={handleClickOpen}>
        <DeleteIcon style={{ color: 'red', fontSize: "30px"  }}/>
      </IconButton>
      <Dialog
        open={open}
        onClose={handleClose}
        aria-labelledby="alert-dialog-title"
        aria-describedby="alert-dialog-description"
      >
        <DialogTitle id="alert-dialog-title">
          {"DBS"}
        </DialogTitle>
        <DialogContent>
          <DialogContentText id="alert-dialog-description">
            Are you sure you would like to delete the selected scheduled transactions?
          </DialogContentText>
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose}>Cancel</Button>
          <Button onClick={handleDelete} autoFocus>
            Confirm
          </Button>
        </DialogActions>
      </Dialog>
    </div>
  );
}

export {ConfirmationPopUp};
