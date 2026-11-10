import { useMemo, useState } from "react";
import type { Transaction } from "../type";
import { formatINR } from "../utils/format";

const PAGE_SIZE = 50;

export default function TransactionsTable({ transactions }: { transactions: Transaction[] }) {
  const [filter, setFilter] = useState("All");
  const [visible, setVisible] = useState(PAGE_SIZE);

  const categories = useMemo(
    () => ["All", ...Array.from(new Set(transactions.map((t) => t.category))).sort()],
    [transactions]
  );

  const filtered = useMemo(
    () => (filter === "All" ? transactions : transactions.filter((t) => t.category === filter)),
    [transactions, filter]
  );

  return (
    <div className="panel">
      <div className="table-header">
        <h2>Transactions ({filtered.length})</h2>
        <select
          aria-label="Filter by category"
          value={filter}
          onChange={(e) => { setFilter(e.target.value); setVisible(PAGE_SIZE); }}
        >
          {categories.map((c) => <option key={c}>{c}</option>)}
        </select>
      </div>

      <table>
        <thead>
          <tr>
            <th>Date</th><th>Description</th><th>Category</th>
            <th className="right">Amount</th><th className="right">Confidence</th>
          </tr>
        </thead>
        <tbody>
          {filtered.slice(0, visible).map((t, i) => (
            <tr key={i}>
              <td>{t.date ?? "-"}</td>
              <td>{t.description}</td>
              <td>
                <span className={t.category === "Uncategorized" ? "badge warn" : "badge"}>
                  {t.category}
                </span>
              </td>
              <td className="right">{formatINR(t.amount)}</td>
              <td className="right">{Math.round(t.confidence * 100)}%</td>
            </tr>
          ))}
        </tbody>
      </table>

      {visible < filtered.length && (
        <button className="more" onClick={() => setVisible((v) => v + PAGE_SIZE)}>
          Show more
        </button>
      )}
    </div>
  );
}