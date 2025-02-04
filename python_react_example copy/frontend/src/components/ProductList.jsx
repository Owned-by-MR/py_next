import React, { useState, useEffect } from 'react';
import { 
    Container, 
    Card, 
    CardContent, 
    Typography, 
    Button,
    CircularProgress,
    Box 
} from '@mui/material';
import axios from 'axios';

const ProductList = () => {
    const [products, setProducts] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        fetchProducts();
    }, []);

    const fetchProducts = async () => {
        try {
            const response = await axios.get('http://localhost:8000/api/products/');
            setProducts(response.data);
            setLoading(false);
        } catch (err) {
            setError(err.message || 'Error fetching products');
            setLoading(false);
            console.error('Error:', err);
        }
    };

    if (loading) return (
        <Container sx={{ display: 'flex', justifyContent: 'center', mt: 4 }}>
            <CircularProgress />
        </Container>
    );

    if (error) return (
        <Container>
            <Box sx={{ mt: 4, p: 2, bgcolor: 'error.light', borderRadius: 1 }}>
                <Typography color="error">Error: {error}</Typography>
            </Box>
        </Container>
    );

    return (
        <Container sx={{ mt: 4 }}>
            <Typography variant="h4" gutterBottom>
                Products
            </Typography>
            <Card container spacing={3}>
                {products.map((product) => (
                    <Card item xs={12} sm={6} md={4} key={product.id}>
                        <Card>
                            <CardContent>
                                <Typography variant="h6" gutterBottom>
                                    {product.name}
                                </Typography>
                                <Typography color="textSecondary" gutterBottom>
                                    SKU: {product.sku}
                                </Typography>
                                <Typography variant="body2" gutterBottom>
                                    Category: {product.category}
                                </Typography>
                                <Typography variant="h6" color="primary" gutterBottom>
                                    ${product.price.toFixed(2)}
                                </Typography>
                                <Typography variant="caption" display="block" gutterBottom>
                                    Added: {new Date(product.created_at).toLocaleDateString()}
                                </Typography>
                            </CardContent>
                        </Card>
                    </Card>
                ))}
            </Card>
        </Container>
    );
};

export default ProductList;
