"""
GreenLink AI - Prototype Geospatial RAG Pipeline (GENIE.AI Compatible)
Use Case: Skopje Green Infrastructure AI Assistant
"""

from dataclasses import dataclass
from typing import List, Dict
import numpy as np

@dataclass
class MunicipalDocument:
    doc_id: str
    parcel_id: str
    title: str
    date: str
    language: str
    content: str

class GreenLinkRAGPrototype:
    def __init__(self, embedding_dim: int = 384):
        self.embedding_dim = embedding_dim
        self.documents: List[MunicipalDocument] = []
        self.vectors: List[np.ndarray] = []

    def _mock_multilingual_embed(self, text: str) -> np.ndarray:
        """
        Placeholder for multilingual embedding model (e.g., BAAI/bge-m3).
        In production, connects to GENIE.AI Embedding Microservice.
        """
        rng = np.random.default_rng(abs(hash(text)) % (2**32))
        vec = rng.normal(size=self.embedding_dim)
        return vec / np.linalg.norm(vec)

    def ingest_document(self, doc: MunicipalDocument) -> None:
        """Indexes municipal record with geospatial parcel metadata."""
        self.documents.append(doc)
        self.vectors.append(self._mock_multilingual_embed(doc.content))

    def retrieve_by_parcel(self, query: str, parcel_id: str = None, top_k: int = 2) -> List[Dict]:
        """Hybrid metadata + semantic similarity retrieval."""
        query_vec = self._mock_multilingual_embed(query)
        scored_results = []

        for doc, vec in zip(self.documents, self.vectors):
            if parcel_id and doc.parcel_id != parcel_id:
                continue
            score = float(np.dot(query_vec, vec))
            scored_results.append({
                "doc_id": doc.doc_id,
                "parcel_id": doc.parcel_id,
                "title": doc.title,
                "date": doc.date,
                "score": round(score, 4),
                "excerpt": doc.content
            })

        scored_results.sort(key=lambda x: x["score"], reverse=True)
        return scored_results[:top_k]

if __name__ == "__main__":
    # Sample Skopje Green Cadastre archival records
    rag = GreenLinkRAGPrototype()
    rag.ingest_document(MunicipalDocument(
        doc_id="SKP-2019-042",
        parcel_id="KP-1042/3",
        title="Botanical Inventory & Protected Canopy Zone - City Park",
        date="2019-06-14",
        language="en",
        content="Parcel KP-1042/3 contains 48 mature deciduous trees designated as protected urban green infrastructure."
    ))
    rag.ingest_document(MunicipalDocument(
        doc_id="SKP-2023-118",
        parcel_id="KP-1042/3",
        title="Municipal Inspection Report - Perimeter Maintenance",
        date="2023-09-22",
        language="en",
        content="No commercial construction permits authorized on Parcel KP-1042/3; buffer zone strictly preserved."
    ))

    results = rag.retrieve_by_parcel("Are construction permits allowed on parcel KP-1042/3?", parcel_id="KP-1042/3")
    for res in results:
        print(f"[{res['doc_id']} | {res['date']}] {res['title']} -> {res['excerpt']}")
