import { useUpload } from "./hooks/useUpload";
import UploadZone from "./Componets/UploadZone";
import axios from "axios";
import SummaryCards from "./Componets/SummaryCards";
import CategoryChart from "./Componets/CategoryChart";
import TransactionsTable from "./Componets/TransactionsTable";

export default function App() {
  const upload = useUpload();

  const errorMessage = axios.isAxiosError(upload.error)
    ? upload.error.response?.data?.detail ?? "Could not reach the API"
    : upload.error
    ? "Something went wrong"
    : null;

  return (
    <div className="container">
      <h1>Smart Expense Analyzer</h1>
      <p className="muted">Upload a bank statement CSV to see where your money goes.</p>

      <UploadZone onFile={(f) => upload.mutate(f)} disabled={upload.isPending} />

      {errorMessage && <p className="error">{errorMessage}</p>}

     {upload.data && (
  <>
    <SummaryCards result={upload.data} />
    <CategoryChart data={upload.data.spending_by_category} />
    <TransactionsTable transactions={upload.data.transactions} />

  </>



)}
    </div>
  );
}