import * as React from 'react';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';
import IconButton from '@mui/material/IconButton';
import AddIcon from '@mui/icons-material/Add';
import { DateTimePicker } from '@mui/x-date-pickers/DateTimePicker';
import { LocalizationProvider } from '@mui/x-date-pickers'
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';

export const AddTransactionDialog = React.forwardRef(() => {
  const [open, setOpen] = React.useState(false);
  const [accountId, setAccountId] = React.useState("");
  const [receivingAccountId, setReceivingAccountId] = React.useState("");
  // const [date, setDate] = React.useState("");
  const [date, setDate] = React.useState(new Date())
  const [amount, setAmount] = React.useState("");
  const [comment, setComment] = React.useState("");
  
  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };
//   const handleAddScheduleTransaction = () => {
//     const addTransaction = async (accountId) => {
//         console.log(`AccountID: ${accountId}`);
//         const payload = {
//             "accountID":accountId
"RECEIBIN"
//         };
//         console.log(payload)
//         try {
//             await axios.post('http://ec2-13-215-211-254.ap-southeast-1.compute.amazonaws.com/transactions/INSERT', payload, {
//               headers: { 
//                 "Authorization": `Bearer ${sessionStorage.getItem("token")}`
//               }
//             })
//               .then((response) => {
//                 console.log(response.data.data)
//                 const mappedData = response.data.data.map(x => createData(x.TransactionID,x.AccountID,x.ReceivingAccountID,x.Date,x.TransactionAmount,x.Comment))
//                 setRows(mappedData)
//               });
//         } catch (err) {
//             console.log(err);
//             return false;
//         }
//     }
//     setOpen(false);
//   };
  

  return (
    <LocalizationProvider dateAdapter={AdapterDayjs}>
    <div>
      <IconButton onClick={handleClickOpen}>
        <AddIcon/>
      </IconButton>
      <Dialog open={open} onClose={handleClose}>
        <DialogTitle>Add Scheduled Transaction</DialogTitle>
        <DialogContent>
          <DialogContentText>
           Please enter the necessary fields to add a new scheduled transaction
          </DialogContentText>
          <TextField
            autoFocus
            margin="dense"
            id="accountId"
            label="Account ID"
            type="text"
            onChange={(newValue) => setAccountId(newValue.target.value)}
            fullWidth
            variant="standard"
          />
          <TextField
            autoFocus
            margin="dense"
            id="receivingAccountId"
            label="Receiving  Account ID"
            type="text"
            onChange={(newValue) => setReceivingAccountId(newValue.target.value)}
            fullWidth
            variant="standard"
          />
          {/* <TextField
            autoFocus
            margin="dense"
            id="date"
            label="Date"
            type="text"
            // onChange={(newValue) => setDate(newValue)}
            fullWidth
            variant="standard"
          /> */}
          <DateTimePicker
          label="Date&Time picker"
          value={date}
          onChange={(newValue) => setDate(newValue)}
          renderInput={(params) => <TextField {...params} />}
          />
          <TextField
            autoFocus
            margin="dense"
            id="amount"
            label="Amount"
            type="text"
            onChange={(newValue) => setAmount(newValue.target.value)}
            fullWidth
            variant="standard"
          />
          <TextField
            autoFocus
            margin="dense"
            id="comment"
            label="Comment"
            type="text"
            onChange={(newValue) => setComment(newValue.target.value)}
            fullWidth
            variant="standard"
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose}>Cancel</Button>
          <Button onClick={handleClose}>Schedule</Button>
        </DialogActions>
      </Dialog>
    </div>
    </LocalizationProvider>
  );
})
