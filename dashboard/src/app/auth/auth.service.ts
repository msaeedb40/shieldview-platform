import { Injectable, inject, PLATFORM_ID } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { BehaviorSubject, tap, Observable } from 'rxjs';
import { isPlatformBrowser } from '@angular/common';

interface AuthResponse {
    access: string;
    refresh: string;
    user?: any;
}

@Injectable({ providedIn: 'root' })
export class AuthService {
    private http = inject(HttpClient);
    private router = inject(Router);
    private platformId = inject(PLATFORM_ID);
    private apiUrl = 'http://localhost:8400/auth'; // Middleware URL

    private loggedIn = new BehaviorSubject<boolean>(this.hasToken());
    isLoggedIn$ = this.loggedIn.asObservable();

    private hasToken(): boolean {
        if (isPlatformBrowser(this.platformId)) {
            return !!localStorage.getItem('access_token');
        }
        return false;
    }

    register(payload: any): Observable<any> {
        return this.http.post(`${this.apiUrl}/register`, payload);
    }

    login(credentials: any): Observable<AuthResponse> {
        return this.http.post<AuthResponse>(`${this.apiUrl}/login`, credentials).pipe(
            tap(res => {
                if (isPlatformBrowser(this.platformId)) {
                    localStorage.setItem('access_token', res.access);
                    localStorage.setItem('refresh_token', res.refresh);
                }
                this.loggedIn.next(true);
                this.router.navigate(['/dashboard']);
            })
        );
    }

    logout() {
        if (isPlatformBrowser(this.platformId)) {
            localStorage.removeItem('access_token');
            localStorage.removeItem('refresh_token');
        }
        this.loggedIn.next(false);
        this.router.navigate(['/login']);
    }

    requestPasswordReset(email: string): Observable<any> {
        return this.http.post(`${this.apiUrl}/password-reset`, { email });
    }

    confirmPasswordReset(payload: any): Observable<any> {
        return this.http.post(`${this.apiUrl}/password-reset/confirm`, payload);
    }

    getToken(): string | null {
        if (isPlatformBrowser(this.platformId)) {
            return localStorage.getItem('access_token');
        }
        return null;
    }
}
