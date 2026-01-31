import { Routes } from '@angular/router';
import { authGuard } from './auth/auth.guard';

export const routes: Routes = [
    { path: 'login', loadComponent: () => import('./auth/login.component').then(m => m.LoginComponent) },
    { path: 'register', loadComponent: () => import('./auth/register.component').then(m => m.RegisterComponent) },
    { path: 'forgot-password', loadComponent: () => import('./auth/forgot-password.component').then(m => m.ForgotPasswordComponent) },
    { path: 'reset-password', loadComponent: () => import('./auth/reset-password.component').then(m => m.ResetPasswordComponent) },
    {
        path: 'dashboard',
        loadComponent: () => import('./dashboard/overview.component').then(m => m.DashboardOverviewComponent),
        canActivate: [authGuard]
    },
    { path: '', redirectTo: '/login', pathMatch: 'full' },
    { path: '**', redirectTo: '/login' }
];
