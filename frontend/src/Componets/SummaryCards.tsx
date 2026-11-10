import { useMemo } from "react";
import type { UploadResult } from "../type";
import { formatINR } from "../utils/format";

export default function SummaryCards({ result }: { result: UploadResult }) {
  const { totalSpend, topCategory } = useMemo(() => {
    const entries = Object.entries(result.spending_by_category);
    const total = entries.reduce((sum, [, amount]) => sum + amount, 0);
    const top = entries
      .filter(([name]) => name !== "Uncategorized")
      .sort((a, b) => b[1] - a[1])[0];
    return { totalSpend: total, topCategory: top?.[0] ?? "-" };
  }, [result]);

  const cards = [
    { label: "Total spend", value: formatINR(totalSpend) },
    { label: "Transactions", value: result.total_transactions.toLocaleString("en-IN") },
    { label: "Top category", value: topCategory },
    { label: "Uncategorized", value: result.uncategorized.toString() },
  ];

  return (
    <div className="cards">
      {cards.map((c) => (
        <div className="card" key={c.label}>
          <p className="muted">{c.label}</p>
          <p className="card-value">{c.value}</p>
        </div>
      ))}
    </div>
  );
}