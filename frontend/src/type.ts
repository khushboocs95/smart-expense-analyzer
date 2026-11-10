export interface Transaction {
  date?: string;
  description: string;
  amount: number;
  category: string;
  confidence: number;
}

export interface UploadResult {
  total_transactions: number;
  uncategorized: number;
  spending_by_category: Record<string, number>;
  transactions: Transaction[];
}